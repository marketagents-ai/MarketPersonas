import os
import json
import glob
import logging
from tqdm import tqdm

from openai import OpenAI
from dotenv import load_dotenv

##############################################################################
# Configuration
##############################################################################

# 1. Load .env file from a custom path
script_dir = os.path.dirname(__file__)
# make sure to add your env file path
dotenv_path = "/home/erebus/Desktop/Sandbox/test/MarketVille/.env"
load_dotenv(dotenv_path=dotenv_path)

# 2. Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_KEY", "missing_key"))

# 3. Choose model, temperature, etc.
OPENAI_MODEL = "gpt-4o-mini"  # Updated to current model name
TEMPERATURE = 0.2
MAX_TOKENS = 200

# 4. Logging configuration
LOG_FILE = "checker.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode='w'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

##############################################################################
# LLM Inference
##############################################################################
def run_openai_llm(prompt: str) -> str:
    """
    Call the OpenAI ChatCompletion endpoint with the user prompt.
    Return the assistant's response as a string.
    """
    try:
        # Basic check if the client has an API key
        if client.api_key == "missing_key":
            raise ValueError("OPENAI_API_KEY is missing or not loaded from .env")
        
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant. You only respond with minimal text. "
                    "Follow the user's instructions carefully."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
        
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=messages,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS
        )
        
        # Extract the text from the first choice
        answer = response.choices[0].message.content.strip()
        return answer
    
    except Exception as e:
        logger.error(f"OpenAI API Error: {e}")
        return "ERROR: OpenAI API call failed."
##############################################################################
# Prompt Generation
##############################################################################
def generate_prompt_for_enum_check(enum_val: str, description: str) -> str:
    """
    Creates a standardized prompt to check if an enum value matches
    its enumDescription logically.
    """
    base_prompt = f"""
You are validating whether the enum value matches its description in a survey schema.

Enum Value: {enum_val}
Enum Description: {description}

Context:
1. The enum values are short codes indicating possible answers.
2. The description is the full text of the answer choice.
3. They should be logically consistent.

Task:
1. Decide if the short enum value logically matches the provided description.
2. If it does, say "Sensible".
3. If it does not, say "Nonsense" and optionally give a one-sentence reason.

Output format:
Sensible or Nonsense
Reason: <short explanation if nonsense>
"""
    return base_prompt.strip()

##############################################################################
# Response Parsing
##############################################################################
def parse_llm_response(response_text: str):
    """
    Attempts to parse the LLM response to get "Sensible" or "Nonsense"
    and the optional reason.
    """
    verdict = "Unknown"
    reason = ""

    # Convert to lower for easier checks
    resp_lower = response_text.lower()

    if "sensible" in resp_lower:
        verdict = "Sensible"
        if "reason:" in resp_lower:
            after_reason = response_text.split("Reason:")[1].strip()
            reason = after_reason
    elif "nonsense" in resp_lower:
        verdict = "Nonsense"
        if "reason:" in resp_lower:
            after_reason = response_text.split("Reason:")[1].strip()
            reason = after_reason

    return verdict, reason

##############################################################################
# Schema Analysis
##############################################################################
def analyze_schema_properties(schema_data: dict) -> list:
    """
    Examine each property in the schema. If it has 'enum' and
    'enumDescriptions', check them with the LLM and parse the results.
    """
    results = []
    properties = schema_data.get("properties", {})

    for prop_name, prop_info in properties.items():
        enum_values = prop_info.get("enum", [])
        enum_descriptions = prop_info.get("enumDescriptions", [])

        # Check if enum and enumDescriptions have the same length
        if len(enum_values) == len(enum_descriptions) and len(enum_values) > 0:
            for enum_val, enum_desc in zip(enum_values, enum_descriptions):
                prompt = generate_prompt_for_enum_check(enum_val, enum_desc)
                response = run_openai_llm(prompt)
                verdict, reason = parse_llm_response(response)

                results.append({
                    "property": prop_name,
                    "enum_value": enum_val,
                    "enum_description": enum_desc,
                    "verdict": verdict,
                    "reason": reason
                })
        else:
            # Mismatch in lengths or missing info
            results.append({
                "property": prop_name,
                "enum_value": None,
                "enum_description": None,
                "verdict": "Skipped",
                "reason": "No matching enum/enumDescriptions or lengths differ."
            })

    return results

##############################################################################
# Main
##############################################################################
def main():
    # Confirm that we have a valid API key loaded
    if client == "missing_key":
        logger.error("OpenAI API key not found. Make sure your .env file is correct.")
        return

    # Directory containing JSON file
    json_dir = os.path.join(script_dir,"./survey_questionnaires/parsed_into_json/gss_schemas")
    
    # Find all JSON files in 'data' directory
    json_files = glob.glob(os.path.join(json_dir, "*.json"))
    
    if not json_files:
        logger.warning(f"No JSON files found in {json_dir}. Please add .json files and rerun.")
        return
    
    logger.info(f"Found {len(json_files)} JSON files in {json_dir}. Beginning analysis...")

    # Use a TQDM progress bar to show progress over JSON files
    for json_file in tqdm(json_files, desc="Processing JSON files", unit="file"):
        logger.info(f"Processing file: {json_file}")

        # Load the JSON schema
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                schema_data = json.load(f)
        except json.JSONDecodeError:
            logger.error(f"Error: {json_file} is not valid JSON.")
            continue
        except Exception as e:
            logger.error(f"Error reading {json_file}: {e}")
            continue

        # Analyze the schema properties
        results = analyze_schema_properties(schema_data)

        # Print or store results
        logger.info(f"Results for {os.path.basename(json_file)}:")
        for r in results:
            prop = r["property"]
            val = r["enum_value"]
            desc = r["enum_description"]
            verdict = r["verdict"]
            reason = r["reason"]

            if verdict in ["Sensible", "Nonsense"]:
                logger.info(
                    f"  - Property: {prop}\n"
                    f"    Enum Value: {val}\n"
                    f"    Description: {desc}\n"
                    f"    Verdict: {verdict}\n"
                    f"    Reason: {reason if reason else 'N/A'}"
                )
            else:
                logger.info(
                    f"  - Property: {prop} => {verdict} ({reason})"
                )

if __name__ == "__main__":
    main()
