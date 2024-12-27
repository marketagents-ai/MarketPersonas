import re
from typing import Dict, List, Optional, Union
from pydantic import BaseModel
import json
import os
from enum import Enum

class QuestionType(str, Enum):
    """Types of survey questions"""
    CATEGORICAL_SINGLE = "Categorical (Single)"
    TEXT = "Text"
    INFO = "Info"
    LONG = "Long"
    
    @classmethod
    def _missing_(cls, value):
        """Handle unknown question types"""
        print(f"Warning: Unknown question type '{value}', defaulting to TEXT")
        return cls.TEXT

class ValidationRule(BaseModel):
    minimum: Optional[int] = None
    maximum: Optional[int] = None

class SurveyQuestion(BaseModel):
    """Represents a single survey question"""
    question_id: str
    question_type: QuestionType
    question_text: str
    page_number: Optional[int] = None
    options: Optional[Dict[str, str]] = None
    validation: Optional[ValidationRule] = None

class SurveySection(BaseModel):
    """Represents a section of the survey"""
    section_id: str
    section_name: str
    questions: List[SurveyQuestion]

def extract_page_number(line: str) -> Optional[int]:
    """Extract page number from the dotted line format"""
    if '.' in line:
        try:
            return int(line.split('.')[-1].strip())
        except ValueError:
            return None
    return None

def parse_question_line(line: str) -> Optional[Dict]:
    """Parse a question definition line"""
    match = re.match(r'^([A-Z][A-Z0-9_]+):\s*(.*?)(?:\s*\.+\s*(\d+)\s*)?$', line)
    if not match:
        return None
    
    question_id, question_type, page = match.groups()
    return {
        'question_id': question_id,
        'question_type': question_type.strip(),
        'page_number': int(page) if page else None
    }

def parse_long_range(question_type: str) -> Optional[ValidationRule]:
    """Parse Long [min .. max] format"""
    match = re.match(r'Long\s*\[(\d+)\s*\.\.\s*(\d+)\]', question_type)
    if match:
        min_val, max_val = map(int, match.groups())
        return ValidationRule(minimum=min_val, maximum=max_val)
    return None

def parse_categorical_question(lines: List[str]) -> Dict:
    """Parse a categorical question and its options"""
    # Skip filter/order lines
    content_lines = [line for line in lines 
                    if not re.match(r'.*\.Categories\.(Filter|Order).*', line)]
    
    # Find where options begin
    try:
        categories_index = content_lines.index('Categories:')
        question_text = ' '.join(line.strip() for line in content_lines[:categories_index] if line.strip())
        options_text = content_lines[categories_index + 1:]
    except ValueError:
        question_text = ' '.join(line.strip() for line in content_lines if line.strip())
        options_text = []

    # Parse options
    options = {}
    codes = []
    descriptions = []
    
    for line in options_text:
        if line.strip():
            if match := re.match(r'{(\w+)}', line.strip()):
                codes.append(match.group(1))
            elif not line.startswith('{'):
                descriptions.append(line.strip())

    # Pair codes with descriptions
    for code, desc in zip(codes, descriptions):
        options[code] = desc

    return {
        'question_text': question_text,
        'options': options
    }

def parse_text_question(lines: List[str]) -> str:
    """Parse a text question"""
    return ' '.join(line.strip() for line in lines if line.strip())

def parse_info_question(lines: List[str]) -> str:
    """Parse an info block"""
    return '\n'.join(line.strip() for line in lines if line.strip())

def parse_long_question(lines: List[str], validation: ValidationRule) -> Dict:
    """Parse a long question"""
    return {
        'question_text': ' '.join(line.strip() for line in lines if line.strip()),
        'validation': validation
    }

def group_questions_by_section(questions: List[SurveyQuestion]) -> Dict[str, List[SurveyQuestion]]:
    """Group questions by their section prefix"""
    sections = {}
    for question in questions:
        # Get section prefix from question ID
        section_prefix = re.match(r'^[A-Z]+', question.question_id).group()
        if section_prefix not in sections:
            sections[section_prefix] = []
        sections[section_prefix].append(question)
    return sections

def generate_schema_for_section(section_id: str, questions: List[SurveyQuestion]) -> Dict:
    """Generate JSON Schema for a section"""
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "title": f"GSS Survey Section: {section_id}",
        "description": f"Questions related to {section_id}",
        "properties": {},
        "required": []
    }

    for question in questions:
        field_schema = {
            "type": "string",
            "title": question.question_id,
            "description": question.question_text
        }

        if question.question_type == QuestionType.CATEGORICAL_SINGLE and question.options:
            field_schema["enum"] = list(question.options.keys())
            field_schema["enumDescriptions"] = list(question.options.values())
        elif question.question_type == QuestionType.LONG and question.validation:
            field_schema["type"] = "integer"
            if question.validation.minimum is not None:
                field_schema["minimum"] = question.validation.minimum
            if question.validation.maximum is not None:
                field_schema["maximum"] = question.validation.maximum

        schema["properties"][question.question_id] = field_schema
        schema["required"].append(question.question_id)

    return schema

def parse_markdown_to_questions(markdown_text: str) -> List[SurveyQuestion]:
    """Parse markdown into list of questions"""
    questions = []
    current_question = None
    current_lines = []
    
    for line in markdown_text.split('\n'):
        line = line.strip()
        
        # Skip empty lines and headers
        if not line or line.startswith('MDDtoDOC') or line == '•':
            continue
            
        # Check for new question
        if question_info := parse_question_line(line):
            # Process previous question if exists
            if current_question and current_lines:
                questions.append(process_question_block(current_question, current_lines))
            
            current_question = question_info
            current_lines = []
        elif current_question:
            current_lines.append(line)
    
    # Process last question
    if current_question and current_lines:
        questions.append(process_question_block(current_question, current_lines))
    
    return questions

def process_question_block(question_info: Dict, lines: List[str]) -> SurveyQuestion:
    """Process a block of lines into a SurveyQuestion"""
    raw_question_type = question_info['question_type']
    validation = None
    options = None
    question_text = ""

    # Determine the question type
    if 'Categorical (Single)' in raw_question_type:
        question_type = QuestionType.CATEGORICAL_SINGLE
        parsed = parse_categorical_question(lines)
        question_text = parsed['question_text']
        options = parsed['options']
    elif 'Long' in raw_question_type:
        question_type = QuestionType.LONG
        validation = parse_long_range(raw_question_type)
        parsed = parse_long_question(lines, validation)
        question_text = parsed['question_text']
    elif 'Text' in raw_question_type:
        question_type = QuestionType.TEXT
        question_text = parse_text_question(lines)
    elif 'Info' in raw_question_type:
        question_type = QuestionType.INFO
        question_text = parse_info_question(lines)
    else:
        # Default to TEXT type for unknown question types
        print(f"Warning: Unknown question type '{raw_question_type}' for question {question_info['question_id']}, defaulting to TEXT")
        question_type = QuestionType.TEXT
        question_text = parse_text_question(lines)

    try:
        return SurveyQuestion(
            question_id=question_info['question_id'],
            question_type=question_type,
            question_text=question_text,
            page_number=question_info.get('page_number'),
            options=options,
            validation=validation
        )
    except Exception as e:
        print(f"Error processing question {question_info['question_id']}: {e}")
        print(f"Raw question type: {raw_question_type}")
        print(f"Processed type: {question_type}")
        print(f"Question text: {question_text}")
        raise

def main():
    """Main function to process GSS survey markdown and generate JSON schemas"""
    input_file = 'survey_questionnaires/parsed_into_markdown/gss_2022.md'
    output_dir = 'survey_questionnaires/parsed_into_json/gss_schemas'
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Read markdown file
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    
    # Parse questions
    questions = parse_markdown_to_questions(markdown_text)
    
    # Group questions by section
    sections = group_questions_by_section(questions)
    
    # Generate and write schemas
    schemas = {}
    for section_id, section_questions in sections.items():
        schema = generate_schema_for_section(section_id, section_questions)
        schemas[section_id] = schema
        
        # Write individual section schema
        output_file = os.path.join(output_dir, f'gss_schema_{section_id.lower()}.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)
    
    # Write combined schema
    combined_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Complete GSS Survey",
        "type": "object",
        "properties": schemas,
        "required": list(schemas.keys())
    }
    
    with open(os.path.join(output_dir, 'gss_schema_complete.json'), 'w', encoding='utf-8') as f:
        json.dump(combined_schema, f, indent=2, ensure_ascii=False)
    
    print(f"Generated {len(schemas)} section schemas")
    print(f"Output directory: {output_dir}")

if __name__ == "__main__":
    main()