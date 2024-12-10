import yaml
import numpy as np
from pydantic import BaseModel
from typing import List, Dict, Any, Union, Optional, Tuple
from pathlib import Path
import names
import random
from copy import deepcopy
import logging
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import argparse
import json

from collections import Counter, defaultdict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ATTRIBUTE_RELATIONSHIPS_FILE = 'config/attribute_relationships.yaml'
ATTRIBUTE_OPTIONS_FILE = 'config/attribute_options.yaml'
ATTRIBUTE_TEMPLATE_FILE = 'config/persona_template.yaml'
PERSONA_MARKDOWN_TEMPLATE = 'config/persona_template.md'

class RetirementManager:
    def __init__(self):
        self._retirement_cache = {}
        self._status_cache = {}
        self._MIN_RETIREMENT_AGE = 65
        self._FORCED_RETIREMENT_AGE = 80
    
    def get_retirement_probability(self, age: int) -> float:
        """Calculate retirement probability with absolute age guards."""
        # Check cache first
        if age in self._retirement_cache:
            return self._retirement_cache[age]
        
        # Absolute guards
        if age < self._MIN_RETIREMENT_AGE:
            prob = 0.0
        elif age >= self._FORCED_RETIREMENT_AGE:
            prob = 1.0
        elif age < 70:
            # Linear scale from 0-30% between 65-70
            prob = ((age - 65) / 5) * 0.3
        else:
            # Cap at 70% for 70+
            prob = min(0.7, 0.3 + ((age - 70) / 10) * 0.4)
        
        self._retirement_cache[age] = prob
        return prob

    def get_retirement_status(self, age: int, current_occupation: str = None, income: float = None) -> Dict[str, Any]:
        """Comprehensive method for all retirement-related information."""
        cache_key = f"{age}_{current_occupation}_{income}"
        if cache_key in self._status_cache:
            return self._status_cache[cache_key]
        
        is_retired = current_occupation == 'Retired'
        prob = self.get_retirement_probability(age)
        should_retire = self.should_be_retired(age, current_occupation)
        
        status = {
            'is_retired': is_retired,
            'should_retire': should_retire,
            'probability': prob,
            'status_text': "Retired" if is_retired else None,
            'income_format': "retirement income" if is_retired else "income",
            'fitness_score': 1.0 if (should_retire == is_retired) else -0.5,
            'formatted_text': self.format_occupation_status(age, current_occupation, income) if income else None,
            'valid_occupation': self.is_valid_retirement_status(age, current_occupation)
        }
        
        self._status_cache[cache_key] = status
        return status

    def should_be_retired(self, age: int, current_occupation: str = None) -> bool:
        """Single source of truth for retirement decisions."""
        # Handle existing retirement
        if current_occupation == 'Retired':
            if age < self._MIN_RETIREMENT_AGE:
                return False  # Force un-retirement for young
            return random.random() < (0.7 if age < 70 else 0.9)
        
        # Force retirement for very elderly
        if age >= self._FORCED_RETIREMENT_AGE:
            return True
            
        # New retirement consideration
        return random.random() < self.get_retirement_probability(age)

    def format_occupation_status(self, age: int, occupation: str, income: float = None) -> Dict[str, str]:
        """Format retirement-related text for display."""
        is_retired = occupation == 'Retired'
        
        status = {
            'occupation_status': "Retired" if is_retired else occupation,
            'occupation_description': "is retired" if is_retired else occupation
        }
        
        if income is not None:
            status['income_status'] = f"has a {'retirement ' if is_retired else ''}income of ${income:,}"
        
        return status

    def is_valid_retirement_status(self, age: int, occupation: str) -> bool:
        """Validate retirement status against age."""
        is_retired = occupation == 'Retired'
        
        if is_retired and age < self._MIN_RETIREMENT_AGE:
            return False
        if age >= self._FORCED_RETIREMENT_AGE and not is_retired:
            return False
            
        return True

    def clear_cache(self):
        """Clear all caches - useful for testing or resetting state."""
        self._retirement_cache.clear()
        self._status_cache.clear()

class Persona(BaseModel):
    name: str
    persona: str
    objectives: List[str]
    metadata: Optional[Dict[str, Any]] = None

class AttributeOptions:
    def __init__(self, yaml_file: str):
        with open(yaml_file, 'r') as file:
            self.options = yaml.safe_load(file)
        
        self._retirement_manager = RetirementManager()  # Add retirement manager
        self._calculate_occupation_distributions()
        self._validate_options()

    def _calculate_occupation_distributions(self):
        """Calculate distribution weights from total_employment values"""
        if 'occupation' not in self.options or 'options' not in self.options['occupation']:
            logger.error("No occupation options found in configuration")
            return

        occupations = self.options['occupation']['options']
        total_employment = 0
        
        # First pass: calculate total employment from income ranges
        # Using midpoint of income range as a proxy for employment level
        for occupation in occupations:
            try:
                if 'valid_income_range' in occupation:
                    min_income, max_income = occupation['valid_income_range']
                    # Use income midpoint as a proxy for employment weight
                    employment_proxy = (min_income + max_income) / 2
                    occupation['total_employment'] = employment_proxy
                    total_employment += employment_proxy
            except (ValueError, TypeError, KeyError) as e:
                logger.warning(f"Error processing employment for {occupation.get('value', 'unknown')}: {e}")
                occupation['total_employment'] = 0

        # Second pass: calculate distribution weights
        if total_employment > 0:
            for occupation in occupations:
                try:
                    employment = occupation.get('total_employment', 0)
                    # Calculate percentage of total workforce
                    occupation['distribution'] = (employment / total_employment)
                    logger.debug(f"Occupation: {occupation['value']}, Distribution: {occupation['distribution']:.4f}")
                except (ValueError, TypeError) as e:
                    logger.warning(f"Error calculating distribution for {occupation.get('value', 'unknown')}: {e}")
                    occupation['distribution'] = 0

        logger.info(f"Calculated distribution weights for {len(occupations)} occupations")

    def _validate_options(self):
        """Validate option configurations"""
        required_attributes = ['age', 'gender', 'education_level', 'occupation', 'income']
        for attr in required_attributes:
            if attr not in self.options:
                raise ValueError(f"Required attribute {attr} missing from options")
            
            # Additional validation for occupation options
            if attr == 'occupation':
                if 'options' not in self.options[attr]:
                    raise ValueError("Occupation options missing from configuration")
                if not self.options[attr]['options']:
                    raise ValueError("Occupation options list is empty")
                
                # Validate each occupation has required fields
                for opt in self.options[attr]['options']:
                    required_fields = ['value', 'valid_education', 'valid_income_range']
                    missing_fields = [field for field in required_fields if field not in opt]
                    if missing_fields:
                        raise ValueError(f"Occupation {opt.get('value', 'unknown')} missing required fields: {missing_fields}")

    def get_random_option(self, attribute: str, persona_data: Dict[str, Any]) -> Any:
        attr_config = self.options.get(attribute)
        if not attr_config:
            logger.warning(f"No configuration found for attribute: {attribute}")
            return None

        if 'options' in attr_config:
            options = attr_config['options']
            if attribute == 'occupation' and len(options) <= 1: 
                raise ValueError("Configuration must include multiple occupation options")
            
            # Updated retirement check using RetirementManager
            if attribute == 'occupation':
                retirement_status = self._retirement_manager.get_retirement_status(
                    persona_data.get('age', 0),
                    persona_data.get('occupation'),
                    persona_data.get('income')
                )
                if retirement_status['should_retire']:
                    return 'Retired'
            
            valid_options = self.filter_options(attribute, options, persona_data)
            
            if not valid_options:
                logger.debug(f"No valid options found for {attribute}, using unfiltered options")
                valid_options = options
                
            if attribute == 'occupation':
                # Get distributions calculated earlier for occupations
                values = [opt['value'] for opt in valid_options]
                # Add debug log to see distributions
                distributions = [opt.get('distribution', 0.0001) for opt in valid_options]
                logger.debug(f"Occupation distributions before normalization: {list(zip(values, distributions))}")
                
                # Normalize the distributions
                total = sum(distributions)
                if total > 0:
                    weights = [d/total for d in distributions]
                    logger.debug(f"Normalized occupation weights: {list(zip(values, weights))}")
                    selected = random.choices(values, weights=weights, k=1)[0]
                    return selected
                
            elif isinstance(valid_options[0], dict):
                # Original dict handling for other attributes
                values = [opt['value'] for opt in valid_options]
                weights = [float(opt.get('distribution', 1)) for opt in valid_options]
                total_weight = sum(weights)
                if total_weight > 0:
                    normalized_weights = [w/total_weight for w in weights]
                    selected = random.choices(values, weights=normalized_weights, k=1)[0]
                    return selected
                    
            return random.choice(valid_options)
            
        elif 'range' in attr_config:
            min_val, max_val = map(float, attr_config['range'].split('-'))
            if attribute in ['openness', 'conscientiousness', 'extraversion', 'agreeableness', 'neuroticism']:
                return self.generate_personality_trait(min_val, max_val)
            return self.generate_ranged_value(attribute, min_val, max_val, persona_data)
            
        return None
    def filter_options(self, attribute: str, options: List[Any], persona_data: Dict[str, Any]) -> List[Any]:
        if attribute == 'occupation':
            valid_occupations = [opt for opt in options if self.is_valid_occupation(opt, persona_data)]
            if not valid_occupations:
                logger.debug("No valid occupations found, returning all options")
                return options
            return valid_occupations
        return options

    def is_valid_occupation(self, occupation: Dict[str, Any], persona_data: Dict[str, Any]) -> bool:
        age = persona_data.get('age', 0)
        education = persona_data.get('education_level', '')
        income = persona_data.get('income', 0)

        # Special case for Retired - only use RetirementManager
        if occupation['value'] == 'Retired':
            return self._retirement_manager.is_valid_retirement_status(
                persona_data.get('age', 0),
                'Retired'
            )
        
        # For non-retirement occupations, check basic requirements
        age_valid = age >= occupation.get('min_age', 0)
        education_valid = education in occupation.get('valid_education', [])
        income_valid = occupation['valid_income_range'][0] <= income <= occupation['valid_income_range'][1]

        return sum([age_valid, education_valid, income_valid]) >= 2

    def generate_personality_trait(self, min_val: float, max_val: float) -> float:
        mean = (min_val + max_val) / 2
        std_dev = (max_val - min_val) / 6
        value = random.gauss(mean, std_dev)
        return round(max(min_val, min(max_val, value)), 2)

    def generate_ranged_value(self, attribute: str, min_val: float, max_val: float, 
                            persona_data: Dict[str, Any]) -> Union[int, float]:
        if attribute == 'age':
            # Modified age distribution to better represent older population
            if random.random() < 0.15:  # 15% chance for retirement-age individual
                # Generate age between 65 and max_val using a different distribution
                return int(65 + (max_val - 65) * (random.random() ** 0.8))
            # Use power distribution for working-age population
            return int(min_val + (max_val - min_val) * (random.random() ** 1.5))
        return random.randint(int(min_val), int(max_val))

class AttributeRelationships:
    def __init__(self, yaml_file: str):
        with open(yaml_file, 'r') as file:
            self.relationships = yaml.safe_load(file)
        self._validate_relationships()

    def _validate_relationships(self):
        """Validate relationship configurations"""
        for attr, config in self.relationships.items():
            if 'relationships' in config:
                for relation in config['relationships']:
                    required_fields = ['secondary_attribute', 'weight']
                    for field in required_fields:
                        if field not in relation:
                            raise ValueError(f"Required field {field} missing in relationship for {attr}")

    def get_weighted_value(self, primary_attr: str, primary_value: Any, 
                          secondary_attr: str, persona_data: Dict[str, Any]) -> List[Union[str, float]]:
        if primary_attr in self.relationships and 'relationships' in self.relationships[primary_attr]:
            for relation in self.relationships[primary_attr]['relationships']:
                if relation['secondary_attribute'] == secondary_attr:
                    if self.check_conditions(relation.get('conditions', []), persona_data):
                        weight = relation['weight']
                        if 'value' in relation:
                            return [relation['value'], abs(weight)]
                        return [primary_value, weight]
        return [primary_value, 1.0]

    def check_conditions(self, conditions: List[str], persona_data: Dict[str, Any]) -> bool:
        return all(self.check_condition(cond, persona_data) for cond in conditions)

    def check_condition(self, condition: str, persona_data: Dict[str, Any]) -> bool:
        operators = ['>=', '<=', '>', '<', '==']
        for op in operators:
            if op in condition:
                attr, value = condition.split(op)
                attr, value = attr.strip(), value.strip()
                attr_value = persona_data.get(attr)
                if attr_value is None:
                    return False
                try:
                    return eval(f"{float(attr_value)} {op} {float(value)}")
                except (ValueError, TypeError):
                    logger.warning(f"Invalid condition evaluation: {condition}")
                    return False
        return True

class PersonaGenerator:
    def __init__(self, relationships: AttributeRelationships, options: AttributeOptions):
        self.relationships = relationships
        self.options = options
        self.attributes = list(options.options.keys())
        self._retirement_manager = RetirementManager()  # Add retirement manager
        self._validate_generator()

    def _validate_generator(self):
        """Validate generator configuration"""
        if not self.attributes:
            raise ValueError("No attributes defined in options")
        
        required_attributes = ['age', 'gender', 'education_level', 'occupation', 'income']
        missing_attributes = [attr for attr in required_attributes if attr not in self.attributes]
        if missing_attributes:
            raise ValueError(f"Missing required attributes: {missing_attributes}")

    def generate_persona(self) -> Persona:
        persona_data = {}
        
        # Generate attributes in a specific order to maintain consistency
        attribute_order = ['age', 'gender', 'education_level', 'occupation', 'income'] + \
                         [attr for attr in self.attributes if attr not in 
                          ['age', 'gender', 'education_level', 'occupation', 'income']]
        
        for attribute in attribute_order:
            if attribute in ['hobbies_and_interests', 'life_events', 'short_term_goals', 
                           'long_term_goals', 'investment_preferences']:
                persona_data[attribute] = [
                    self.generate_attribute(attribute, persona_data) 
                    for _ in range(min(1, len(self.options.options[attribute].get('options', []))))
                ]
            else:
                persona_data[attribute] = self.generate_attribute(attribute, persona_data)

        name = names.get_full_name(gender=persona_data['gender'].lower())
        role = persona_data['role']
        
        # Format persona text
        persona = self.format_persona(persona_data, name)
                
        # Replace the hardcoded objectives with
        objectives = []
        if 'objectives' in self.options.options:
            valid_objectives = [obj for obj in self.options.options['objectives']['options'] 
                            if self.options.filter_options('objectives', [obj], persona_data)]
            objectives = [obj['value'] for obj in valid_objectives]
        
        return Persona(
            name=name,
            role=role,
            persona=persona,
            objectives=objectives,
            metadata={'raw_data': persona_data}
        )

    def generate_attribute(self, attribute: str, persona_data: Dict[str, Any]) -> Any:
        if attribute == 'education_level' and 'occupation' in persona_data:
            # Get occupation options
            occupation_options = self.options.options['occupation']['options']
            current_occupation = next(
                (opt for opt in occupation_options if opt['value'] == persona_data['occupation']),
                None
            )
            
            if current_occupation and 'valid_education' in current_occupation:
                # Use valid education levels from occupation config
                valid_education = current_occupation['valid_education']
                return random.choice(valid_education)
        
        # Original attribute generation logic
        value = self.options.get_random_option(attribute, persona_data)
        if value is None:
            logger.warning(f"Failed to generate value for attribute: {attribute}")
            return None

        # Apply relationship constraints
        if attribute in self.relationships.relationships and \
           'relationships' in self.relationships.relationships[attribute]:
            for relation in self.relationships.relationships[attribute]['relationships']:
                secondary_attr = relation['secondary_attribute']
                weighted_value, weight = self.relationships.get_weighted_value(
                    attribute, value, secondary_attr, persona_data
                )
                
                if random.random() < abs(weight):
                    if isinstance(weighted_value, str):
                        value = weighted_value
                    elif weight < 0:
                        # Handle inverse relationships
                        options = self.options.options[attribute].get('options', [])
                        if options:
                            opposite_index = (options.index(weighted_value) + len(options) // 2) % len(options)
                            value = options[opposite_index]
                        elif isinstance(weighted_value, (int, float)):
                            attr_config = self.options.options[attribute]
                            if 'range' in attr_config:
                                min_val, max_val = map(float, attr_config['range'].split('-'))
                                value = min_val + max_val - weighted_value
                    else:
                        value = weighted_value

        # Normalize values
        if isinstance(value, float) and attribute not in ['openness', 'conscientiousness', 
                                                        'extraversion', 'agreeableness', 'neuroticism']:
            value = int(round(value))
        elif isinstance(value, float):
            value = round(value, 2)

        return value

    def format_persona(self, persona_data: Dict[str, Any], name: str) -> str:
        try:
            with open(ATTRIBUTE_TEMPLATE_FILE, 'r', encoding='utf-8') as file:
                template_data = yaml.safe_load(file)
                
            # Get retirement status and formatted text
            retirement_status = self._retirement_manager.get_retirement_status(
                persona_data.get('age', 0),
                persona_data.get('occupation'),
                persona_data.get('income')
            )
            
            if retirement_status['formatted_text']:
                formatted_status = retirement_status['formatted_text']
                persona_data['occupation_status'] = formatted_status['occupation_status']
                persona_data['income_status'] = formatted_status['income_status']
            else:
                # Fallback formatting if needed
                if persona_data['occupation'] == 'Unemployed':
                    persona_data['occupation_status'] = "is currently unemployed"
                    persona_data['income_status'] = "currently has minimal income"
                else:
                    persona_data['occupation_status'] = f"{persona_data['occupation']}"
                    persona_data['income_status'] = f"${persona_data['income']:,}"
            
            # Format the template string with persona data
            formatted_text = template_data['template'].format(
                name=name,
                **persona_data
            )
            
            # Clean up the formatted text for description and narrative fields
            formatted_yaml = yaml.safe_load(formatted_text)
            if 'description' in formatted_yaml:
                formatted_yaml['description'] = formatted_yaml['description'].strip()
            if 'narrative' in formatted_yaml:
                formatted_yaml['narrative'] = formatted_yaml['narrative'].strip()
            
            return yaml.dump(formatted_yaml, default_flow_style=False)
            
        except Exception as e:
            logger.error(f"Error formatting persona: {e}")
            raise

    def validate_occupation_constraints(self, persona_data: Dict[str, Any]) -> bool:
        """Validate occupation-specific constraints"""
        occupation = persona_data.get('occupation')
        if not occupation:
            return True
        
        occupation_config = next(
            (opt for opt in self.options.get_options('occupation') 
             if opt['value'] == occupation),
            None
        )
        
        if occupation_config:
            # Update retirement check to use manager
            if occupation == 'Retired':
                age = persona_data.get('age', 0)
                return self._retirement_manager.get_retirement_probability(age) > 0
            
            # Validate education
            if persona_data.get('education_level') not in occupation_config['valid_education']:
                return False
            
            # Validate income range
            income = persona_data.get('income', 0)
            min_income, max_income = occupation_config['valid_income_range']
            if not (min_income <= income <= max_income):
                return False
            
            # Validate age
            if persona_data.get('age', 0) < occupation_config['min_age']:
                return False
            
        return True

class DivergentTreeSampler:
    def __init__(self, base_generator: PersonaGenerator, num_iterations: int = 1000, 
                 burn_in: int = 100, exploration_rate: float = 0.1):
        self.base_generator = base_generator
        self.num_iterations = num_iterations
        self.burn_in = burn_in
        self.exploration_rate = exploration_rate
        self.current_state = None
        self.chain_history = []
        self.acceptance_history = []
        self._validate_wandering_params()
        self._retirement_manager = RetirementManager()  # Add retirement manager

    def _validate_wandering_params(self):
        """Validate DTS parameters"""
        if self.burn_in >= self.num_iterations:
            raise ValueError("burn_in must be less than num_iterations")
        if not 0 < self.exploration_rate < 1:
            raise ValueError("exploration_rate must be between 0 and 1")

    def fitness(self, persona_data: Dict[str, Any]) -> float:
        """Enhanced fitness calculation with consistent retirement handling"""
        # First check hard constraints
        if not self._check_hard_constraints(persona_data):
            return 0.0
        
        score = 0.0
        
        # Get retirement status and add its fitness score
        retirement_status = self._retirement_manager.get_retirement_status(
            persona_data.get('age', 0),
            persona_data.get('occupation')
        )
        score += retirement_status['fitness_score']
        
        # Process all other relationships as before
        for attr, config in self.base_generator.relationships.relationships.items():
            if attr != 'age' and 'relationships' in config:  # Skip age since we handled it
                for relation in config['relationships']:
                    primary_value = persona_data.get(attr)
                    secondary_attr = relation['secondary_attribute']
                    secondary_value = persona_data.get(secondary_attr)
                    
                    if primary_value is not None and secondary_value is not None:
                        weighted_value, weight = self.base_generator.relationships.get_weighted_value(
                            attr, primary_value, secondary_attr, persona_data
                        )
                        
                        if isinstance(primary_value, (int, float)) and isinstance(weighted_value, (int, float)):
                            diff = abs(primary_value - weighted_value)
                            max_val = max(abs(primary_value), abs(weighted_value), 1)
                            score += weight * (1 - diff / max_val)
                        elif primary_value == weighted_value:
                            score += weight
                        else:
                            score -= abs(weight)
        
        return np.exp(score / (len(self.base_generator.relationships.relationships) + 1))

    def _check_hard_constraints(self, persona_data: Dict[str, Any]) -> bool:
        """Check hard constraints from attribute_options.yaml"""
        try:
            # Occupation constraints (removing retirement checks)
            occupation = persona_data.get('occupation')
            if occupation and occupation != 'Retired':  # Skip checks for Retired
                occupation_config = next(
                    (opt for opt in self.base_generator.options.options['occupation']['options'] 
                    if opt['value'] == occupation),
                    None
                )
                if occupation_config:
                    # Only check basic occupation validity, not retirement
                    age = persona_data.get('age', 0)
                    education = persona_data.get('education_level', '')
                    income = persona_data.get('income', 0)
                    
                    age_valid = age >= occupation_config.get('min_age', 0)
                    education_valid = education in occupation_config.get('valid_education', [])
                    income_valid = occupation_config['valid_income_range'][0] <= income <= occupation_config['valid_income_range'][1]
                    
                    if not (sum([age_valid, education_valid, income_valid]) >= 2):
                        return False

            # Rest of constraints remain the same...
            # Check for duplicate values in lists
            for attr, value in persona_data.items():
                if isinstance(value, list) and len(value) != len(set(value)):
                    return False

            # Range constraints for numeric attributes (except age)
            for attr, value in persona_data.items():
                if attr == 'age':
                    continue
                if attr in self.base_generator.options.options:
                    attr_config = self.base_generator.options.options[attr]
                    if 'range' in attr_config:
                        min_val, max_val = map(float, attr_config['range'].split('-'))
                        if not (min_val <= float(value) <= max_val):
                            return False

            return True
        except Exception as e:
            logger.error(f"Error checking constraints: {e}")
            return False

    def propose_new_state(self, current_state: Dict[str, Any]) -> Dict[str, Any]:
        """Propose new state with consistent retirement handling"""
        max_attempts = 10
        for _ in range(max_attempts):
            new_state = deepcopy(current_state)
            
            # Determine number of attributes to modify
            if self.acceptance_history:
                recent_acceptance_rate = np.mean(self.acceptance_history[-50:])
                num_attributes_to_modify = max(1, min(
                    4,
                    int(1 + 3 * (1 - recent_acceptance_rate))
                ))
            else:
                num_attributes_to_modify = np.random.randint(1, 4)
            
            # Select attributes to modify
            relationship_attrs = set(self.base_generator.relationships.relationships.keys())
            other_attrs = set(self.base_generator.attributes) - relationship_attrs
            
            all_attrs = list(relationship_attrs) + list(other_attrs)
            weights = [2 if attr in relationship_attrs else 1 for attr in all_attrs]
            
            attributes_to_modify = np.random.choice(
                all_attrs,
                size=min(num_attributes_to_modify, len(all_attrs)),
                replace=False,
                p=np.array(weights) / sum(weights)
            )
            
            # Modify selected attributes using base generator's methods
            for attr in attributes_to_modify:
                if attr == 'occupation':
                    retirement_status = self._retirement_manager.get_retirement_status(
                        new_state.get('age', 0),
                        new_state.get('occupation')
                    )
                    if retirement_status['should_retire']:
                        new_state['occupation'] = 'Retired'
                    else:
                        # Only get new occupation if not retired
                        new_value = self.base_generator.options.get_random_option(attr, new_state)
                        if new_value != 'Retired':  # Double-check we don't override retirement
                            new_state[attr] = new_value
                else:
                    new_value = self.base_generator.options.get_random_option(attr, new_state)
                    new_state[attr] = new_value
            
            # Check if the new state satisfies constraints
            if self._check_hard_constraints(new_state):
                return new_state
        
        # If we couldn't generate a valid state, return the current state
        return current_state

    def wander_tree(self) -> List[Dict[str, Any]]:
        """Wander the tree, generating a chain of divergent but constrained child"""
        # Initialize with a random persona
        self.current_state = {
            'metadata': {
                'wandering_iteration': 0,
                'acceptance_rate': 0.0,
                'fitness_score': 0.0,
            }
        }
        
        # Generate initial attributes
        for attr in self.base_generator.attributes:
            if attr in ['hobbies_and_interests', 'life_events', 'short_term_goals', 
                    'long_term_goals', 'investment_preferences']:
                self.current_state[attr] = [
                    self.base_generator.generate_attribute(attr, self.current_state)
                    for _ in range(1)
                ]
            else:
                self.current_state[attr] = self.base_generator.generate_attribute(
                    attr, self.current_state
                )
        
        # Calculate initial fitness
        self.current_state['metadata']['fitness_score'] = self.fitness(self.current_state)
        
        self.chain_history = [deepcopy(self.current_state)]
        self.acceptance_history = []
        accepted_count = 0
        
        # Run DTS iterations with metadata tracking
        for i in range(self.num_iterations):
            if i % 100 == 0:
                logger.info(f"DTS iteration {i}/{self.num_iterations}")
            
            try:
                # Generate proposed state with metadata
                proposed_state = self.propose_new_state(self.current_state)
                proposed_state['metadata'] = {
                    'wandering_iteration': i,
                    'acceptance_rate': accepted_count / (i + 1) if i > 0 else 0.0,
                    'fitness_score': self.fitness(proposed_state)
                }
                
                # Calculate acceptance probability
                acceptance_prob = self.divergence_probability(self.current_state, proposed_state)
                
                # Debug logging
                if i % 100 == 0:
                    logger.debug(f"Proposed state fitness: {proposed_state['metadata']['fitness_score']}")
                    logger.debug(f"Current state fitness: {self.current_state['metadata']['fitness_score']}")
                    logger.debug(f"Acceptance probability: {acceptance_prob}")
                
                # Determine acceptance
                accepted = random.random() < acceptance_prob
                self.acceptance_history.append(accepted)
                
                if accepted:
                    self.current_state = deepcopy(proposed_state)
                    accepted_count += 1
                    if i % 100 == 0:
                        logger.debug("State accepted!")
                
                # Update metadata for current state
                self.current_state['metadata'].update({
                    'wandering_iteration': i,
                    'acceptance_rate': accepted_count / (i + 1),
                    'fitness_score': self.fitness(self.current_state)
                })
                
                # Always append a deep copy to chain history
                self.chain_history.append(deepcopy(self.current_state))
                
            except Exception as e:
                logger.error(f"Error in DTS iteration {i}: {e}")
                continue
        
        logger.info(f"DTS completed. Final acceptance rate: {accepted_count/self.num_iterations:.2f}")
        
        # Return chain after burn-in with verification
        final_chain = self.chain_history[self.burn_in:]
        logger.info(f"Chain length after burn-in: {len(final_chain)}")
        logger.info(f"Number of unique states: {len({str(state) for state in final_chain})}")
        
        return final_chain

    def generate_personas(self, num_personas: int) -> List[Persona]:
        """Generate personas using DTS sampling with enhanced diversity checks"""
        logger.info(f"Generating {num_personas} personas using DTS")
        
        # Run DTS if needed
        if not self.chain_history:
            logger.info("Running DTS chain...")
            chain = self.wander_tree()
        else:
            chain = self.chain_history[self.burn_in:]
        
        # Verify chain diversity
        unique_states = len({str(state) for state in chain})
        logger.info(f"Number of unique states in chain: {unique_states}")
        
        if unique_states < num_personas:
            logger.warning(f"Chain has only {unique_states} unique states, running additional iterations")
            # Run additional iterations if needed
            self.num_iterations += 1000
            chain = self.wander_tree()
        
        # Calculate optimal thinning
        thinning = max(1, len(chain) // (num_personas * 2))
        thinned_chain = chain[::thinning]
        
        logger.info(f"Sampling {num_personas} personas from chain of length {len(chain)} (thinning={thinning})")
        
        # Sample with diversity check
        personas = []
        max_attempts = num_personas * 2
        attempts = 0
        used_states = set()
        
        while len(personas) < num_personas and attempts < max_attempts:
            try:
                # Sample a random state
                state_idx = random.randrange(len(thinned_chain))
                state = thinned_chain[state_idx]
                
                # Check if this state is too similar to existing personas
                state_key = str(state)
                if state_key in used_states:
                    attempts += 1
                    continue
                
                # Generate persona from state
                name = names.get_full_name(gender=state['gender'].lower())
                role = state['role']
                persona_text = self.base_generator.format_persona(state, name)
                
                # Add DTS-specific metadata
                metadata = {
                    'raw_data': state,
                    'wandering_iteration': state_idx * thinning + self.burn_in,
                    'fitness_score': self.fitness(state),
                    'acceptance_rate': sum(self.acceptance_history) / len(self.acceptance_history),
                    'chain_position': state_idx
                }
                
                # This shouldn't be hardcoded like it is, it should inherit from the options in yaml with conditions

                persona = Persona(
                    name=name,
                    role=role,
                    persona=persona_text,
                    objectives=[
                        f"{'Purchase' if role == 'Buyer' else 'Sell'} goods at favorable prices",
                        f"Your goal is to {'maximize utility' if role == 'Buyer' else 'maximize profits'}"
                    ],
                    metadata=metadata
                )
                
                personas.append(persona)
                used_states.add(state_key)
                
                if len(personas) % 10 == 0:
                    logger.info(f"Generated {len(personas)} personas...")
                
            except Exception as e:
                logger.error(f"Error generating persona: {e}")
                attempts += 1
                continue
        
        if len(personas) < num_personas:
            logger.warning(f"Could only generate {len(personas)} unique personas")
        
        return personas

    def divergence_probability(self, current: Dict[str, Any], proposed: Dict[str, Any]) -> float:
        """Calculate acceptance probability with enhanced debugging"""
        try:
            # Check if states are different
            if current == proposed:
                logger.debug("Proposed state identical to current state")
                return 0.0
            
            current_fitness = self.fitness(current)
            proposed_fitness = self.fitness(proposed)
            
            # Debug fitnesss
            logger.debug(f"Current fitness: {current_fitness}")
            logger.debug(f"Proposed fitness: {proposed_fitness}")
            
            if current_fitness == 0:
                return 1.0
            
            # Calculate acceptance probability
            prob = min(1.0, proposed_fitness / current_fitness)
            
            # Add randomness to prevent getting stuck
            if prob < 0.1:  # If very low probability
                prob = max(prob, 0.1)  # Ensure at least 10% chance
            
            return prob
            
        except Exception as e:
            logger.error(f"Error calculating acceptance probability: {e}")
            return 0.0
    

def save_persona_to_file(persona: Persona, metadata: Dict[str, Any], output_dir: Path):
    """
    Save persona data in multiple formats and generation logs separately.
    
    Args:
        persona: Persona object containing the generated data
        metadata: Dictionary containing generation metadata and raw data
        output_dir: Base directory for all output files
    
    Creates:
        - persona data in yaml/json/markdown formats
        - generation logs in separate log directory
    """
    # Set up directory structure
    format_dirs = {
        'yaml': output_dir / 'yaml',
        'json': output_dir / 'json',
        'md': output_dir / 'markdown',
        'logs': output_dir / 'logs'  # Add logs directory
    }
    for dir_path in format_dirs.values():
        dir_path.mkdir(parents=True, exist_ok=True)

    # Generate base filename
    base_filename = persona.name.replace(' ', '_')

    # 1. Save Generation Logs
    generation_info = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "persona_name": persona.name,
        "wandering_metrics": {
            "iteration": metadata.get('raw_data', {}).get('metadata', {}).get('wandering_iteration', 0),
            "acceptance_rate": f"{metadata.get('raw_data', {}).get('metadata', {}).get('acceptance_rate', 0):.2%}",
            "fitness_score": f"{metadata.get('raw_data', {}).get('metadata', {}).get('fitness_score', 0):.2f}"
        }
    }

    # Save detailed generation log
    with open(format_dirs['logs'] / f"{base_filename}.log", "w", encoding='utf-8') as f:
        f.write("## Generation Information\n")
        f.write(f"- Timestamp: {generation_info['timestamp']}\n")
        f.write(f"- Persona Name: {generation_info['persona_name']}\n")  # Fixed f-string
        f.write("- DTS Metrics:\n")
        for k, v in generation_info['wandering_metrics'].items():
            f.write(f"  - {k.replace('_', ' ').title()}: {v}\n")

    # 2. Prepare Persona Data
    # Load YAML template
    with open(ATTRIBUTE_TEMPLATE_FILE, 'r', encoding='utf-8') as f:
        template_data = yaml.safe_load(f)

    # Format occupation text
    raw_data = metadata.get('raw_data', {})
    raw_occupation = raw_data.get('occupation')
    occupation = (
        "is currently unemployed" if raw_occupation == 'Unemployed'
        else "is retired" if raw_occupation == 'Retired'
        else f"{raw_occupation}"
    )

    # Create format dictionary
    format_dict = {
        'name': persona.name,
        'occupation': occupation,
        **{k: v for k, v in raw_data.items() 
           if v is not None and k != 'occupation'}
    }

    # Format template with persona data
    formatted_text = template_data['template'].format(**format_dict)
    template_style_data = yaml.safe_load(formatted_text)

    # Build final output data
    output_data = {}
    
    # Preserve multi-line strings and style
    for key, value in template_style_data.items():
        output_data[key] = value.strip() if isinstance(value, str) else value

    # Add objectives if present
    if persona.objectives:
        output_data["objectives"] = persona.objectives

    # 3. Save Persona Data Files
    # YAML format with style preservation
    yaml.add_representer(
        str, 
        lambda dumper, data: dumper.represent_scalar(
            'tag:yaml.org,2002:str', 
            data, 
            style='|' if '\n' in data else None
        )
    )
    
    with open(format_dirs['yaml'] / f"{base_filename}.yaml", "w", encoding='utf-8') as f:
        yaml.safe_dump(
            output_data,
            f,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False,
            indent=2,
            width=None
        )

    # JSON format
    with open(format_dirs['json'] / f"{base_filename}.json", "w", encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    # Markdown format with template
    try:
        with open(PERSONA_MARKDOWN_TEMPLATE, 'r', encoding='utf-8') as f:
            md_template = f.read()

        # Get raw lists without bullet points (template will add them)
        raw_lists = {
            'hobbies_and_interests': raw_data.get('hobbies_and_interests', []),
            'life_events': raw_data.get('life_events', []),
            'short_term_goals': raw_data.get('short_term_goals', []),
            'long_term_goals': raw_data.get('long_term_goals', []),
            'values': raw_data.get('values', [])
        }

        # Create markdown format dictionary
        md_format_dict = {
            **format_dict,  # Base fields
            **raw_lists,    # List fields
            'description': output_data.get('description', ''),
            'narrative': output_data.get('narrative', '')
        }

        # Add objectives if present
        if persona.objectives:
            md_format_dict['objectives'] = '\n'.join(f"- {obj}" for obj in persona.objectives)
        else:
            md_format_dict['objectives'] = ''

        # Format markdown using template
        formatted_markdown = md_template.format(**md_format_dict)
        
        with open(format_dirs['md'] / f"{base_filename}.md", "w", encoding='utf-8') as f:
            f.write(formatted_markdown)

    except (FileNotFoundError, KeyError) as e:
        logger.warning(f"Failed to use markdown template ({str(e)}), falling back to default format")
        
        # Original fallback formatting
        with open(format_dirs['md'] / f"{base_filename}.md", "w", encoding='utf-8') as f:
            f.write(f"# {persona.name}\n\n")
            
            for section, content in output_data.items():
                f.write(f"## {section.replace('_', ' ').title()}\n")
                
                if isinstance(content, dict):
                    for k, v in content.items():
                        if isinstance(v, list):
                            f.write(f"### {k.replace('_', ' ').title()}\n")
                            for item in v:
                                f.write(f"- {item}\n")
                        else:
                            f.write(f"- {k.replace('_', ' ').title()}: {v}\n")
                elif isinstance(content, list):
                    for item in content:
                        f.write(f"- {item}\n")
                else:
                    f.write(f"{content}\n")
                f.write("\n")

class Visualizer:
    def __init__(self, chain_history: List[Dict[str, Any]], acceptance_history: List[bool], burn_in: int):
        self.chain_history = chain_history
        self.acceptance_history = acceptance_history
        self.burn_in = burn_in

    def plot_wandering_diagnostics(self) -> Tuple[plt.Figure, plt.Figure]:
        """Generate diagnostic plots for the DTS chain using matplotlib only"""
        # Create two figures
        fig1, axes1 = plt.subplots(2, 1, figsize=(12, 8))
        fig2, axes2 = plt.subplots(2, 2, figsize=(15, 10))
        
        # Plot 1: Acceptance Rate Over Time
        window_size = 100
        rolling_acceptance = pd.Series(self.acceptance_history).rolling(window=window_size).mean()
        axes1[0].plot(rolling_acceptance)
        axes1[0].set_title(f'Rolling Acceptance Rate (window={window_size})')
        axes1[0].set_xlabel('Iteration')
        axes1[0].set_ylabel('Acceptance Rate')
        
        # Plot 2: fitness Evolution
        fitnesss = [state['metadata']['fitness_score'] for state in self.chain_history]
        axes1[1].plot(fitnesss)
        axes1[1].axvline(x=self.burn_in, color='r', linestyle='--', label='Burn-in')
        axes1[1].set_title('fitness Evolution')
        axes1[1].set_xlabel('Iteration')
        axes1[1].set_ylabel('fitness Score')
        axes1[1].legend()
        
        # Plot 3: Age Distribution Evolution
        ages_pre = [state['age'] for state in self.chain_history[:self.burn_in]]
        ages_post = [state['age'] for state in self.chain_history[self.burn_in:]]
        axes2[0,0].hist([ages_pre, ages_post], label=['Pre burn-in', 'Post burn-in'], 
                        alpha=0.5, bins=30)
        axes2[0,0].set_title('Age Distribution Evolution')
        axes2[0,0].set_xlabel('Age')
        axes2[0,0].set_ylabel('Frequency')
        axes2[0,0].legend()
        
        # Plot 4: Income Distribution Evolution
        incomes_pre = [state['income'] for state in self.chain_history[:self.burn_in]]
        incomes_post = [state['income'] for state in self.chain_history[self.burn_in:]]
        axes2[0,1].hist([incomes_pre, incomes_post], label=['Pre burn-in', 'Post burn-in'], 
                        alpha=0.5, bins=30)
        axes2[0,1].set_title('Income Distribution Evolution')
        axes2[0,1].set_xlabel('Income')
        axes2[0,1].set_ylabel('Frequency')
        axes2[0,1].legend()
        
        # Plot 5: Occupation Changes
        occupations = pd.Series([state['occupation'] for state in self.chain_history])
        occupation_counts = occupations.value_counts()
        axes2[1,0].bar(range(len(occupation_counts)), occupation_counts.values)
        axes2[1,0].set_xticks(range(len(occupation_counts)))
        axes2[1,0].set_xticklabels(occupation_counts.index, rotation=45, ha='right')
        axes2[1,0].set_title('Occupation Distribution')
        axes2[1,0].set_ylabel('Frequency')
                
        # Plot 6: Personality Traits Web Chart
        axes2[1,1].remove()  # Remove the existing axes
        ax_web = fig2.add_subplot(224, projection='polar')

        # Define traits and generations
        personality_traits = ['openness', 'conscientiousness', 'extraversion', 'agreeableness', 'neuroticism']
        generations = [
            {'name': '18-25', 'range': (18, 25), 'color': 'b'},
            {'name': '26-40', 'range': (26, 40), 'color': 'g'},
            {'name': '41-55', 'range': (41, 55), 'color': 'r'},
            {'name': '56+', 'range': (56, 100), 'color': 'purple'}
        ]

        # Set up the angles for the web chart (convert to radians)
        angles = np.linspace(0, 2*np.pi, len(personality_traits), endpoint=False)

        # Plot for each generation
        for gen in generations:
            trait_means = []
            # Filter data for this generation
            gen_data = [state for state in self.chain_history[self.burn_in:] 
                        if gen['range'][0] <= state['age'] <= gen['range'][1]]
            
            if gen_data:  # Only plot if we have data for this generation
                # Calculate means for each trait
                for trait in personality_traits:
                    trait_values = [state[trait] for state in gen_data]
                    trait_means.append(np.mean(trait_values))
                
                # Close the plot by appending first value
                trait_means.append(trait_means[0])
                angles_plot = np.concatenate((angles, [angles[0]]))
                
                # Plot the web chart
                ax_web.plot(angles_plot, trait_means, 'o-', color=gen['color'], 
                        label=f"{gen['name']} (n={len(gen_data)})")
                ax_web.fill(angles_plot, trait_means, alpha=0.25, color=gen['color'])

        # Set the labels
        ax_web.set_xticks(angles)
        ax_web.set_xticklabels([trait.capitalize() for trait in personality_traits])

        # Set the chart title and legend
        ax_web.set_title('Personality Traits by Generation')
        ax_web.legend(bbox_to_anchor=(0.1, 0.1))

        # Adjust layout
        fig1.tight_layout()
        fig2.tight_layout()
        
        return fig1, fig2
        
    def plot_personality_analysis(self) -> plt.Figure:
        """Generate personality trait analysis visualization with generational breakdown"""
        trait_fig = plt.figure(figsize=(15, 10))
        personality_traits = ['openness', 'conscientiousness', 'extraversion', 'agreeableness', 'neuroticism']
        
        # Define generations
        generations = [
            {'name': '18-25', 'range': (18, 25), 'color': 'b'},
            {'name': '26-40', 'range': (26, 40), 'color': 'g'},
            {'name': '41-55', 'range': (41, 55), 'color': 'r'},
            {'name': '56+', 'range': (56, 100), 'color': 'purple'}
        ]
        
        for idx, trait in enumerate(personality_traits, 1):
            ax = trait_fig.add_subplot(2, 3, idx)
            
            # Collect data for each generation
            gen_data = []
            labels = []
            for gen in generations:
                # Filter data for this generation
                values = [state[trait] for state in self.chain_history[self.burn_in:]
                        if gen['range'][0] <= state['age'] <= gen['range'][1]]
                if values:  # Only add if we have data
                    gen_data.append(values)
                    labels.append(f"{gen['name']} (n={len(values)})")
            
            # Create violin plot
            parts = ax.violinplot(gen_data, showmeans=True)
            
            # Customize violin plots for each generation
            for i, pc in enumerate(parts['bodies']):
                pc.set_facecolor(generations[i]['color'])
                pc.set_alpha(0.6)
            parts['cmeans'].set_color('black')
            
            # Calculate overall statistics
            all_values = [v for gen_list in gen_data for v in gen_list]
            mean_val = np.mean(all_values)
            std_val = np.std(all_values)
            
            # Add reference lines for overall statistics
            ax.axhline(mean_val, color='black', linestyle='--', alpha=0.5,
                    label=f'Overall Mean: {mean_val:.2f}')
            ax.axhline(mean_val + std_val, color='gray', linestyle=':', alpha=0.5,
                    label=f'Overall ±1 SD: {std_val:.2f}')
            ax.axhline(mean_val - std_val, color='gray', linestyle=':', alpha=0.5)
            
            # Customize plot
            ax.set_title(f'{trait.capitalize()} Distribution by Generation')
            ax.set_ylabel('Score')
            ax.set_xticks(range(1, len(labels) + 1))
            ax.set_xticklabels(labels, rotation=45, ha='right')
            ax.grid(True, alpha=0.3)
            
            # Add statistics box with generational means
            stats_text = ["Overall:"]
            stats_text.append(f"Mean: {mean_val:.2f}")
            stats_text.append(f"Std: {std_val:.2f}")
            stats_text.append("\nBy Generation:")
            for i, gen_values in enumerate(gen_data):
                gen_mean = np.mean(gen_values)
                stats_text.append(f"{generations[i]['name']}: {gen_mean:.2f}")
            
            ax.text(0.95, 0.05, "\n".join(stats_text),
                transform=ax.transAxes,
                fontsize=8,
                verticalalignment='bottom',
                horizontalalignment='right',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
            
            # Add legend
            ax.legend(fontsize=8)
        
        # Add title and adjust layout
        trait_fig.suptitle('Personality Trait Analysis by Generation',
                        fontsize=14, fontweight='bold')
        trait_fig.tight_layout()
        
        return trait_fig

    def save_visualization(self, output_dir: Path):
        """Save DTS diagnostic visualizations and personality analysis"""
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate plots
        fig1, fig2 = self.plot_wandering_diagnostics()
        # Save all figures
        fig1.savefig(output_dir / 'wandering_diagnostics_1.png', dpi=300, bbox_inches='tight')
        fig2.savefig(output_dir / 'wandering_diagnostics_2.png', dpi=300, bbox_inches='tight')
        
        plt.close('all')

def load_occupation_data(json_file: str) -> Dict[str, Dict]:
    """Load and process occupation data from JSON file"""
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        processed_data = {}
        for occupation in data:
            try:
                # Clean and validate income data
                annual_income_str = occupation['annual_median_income']
                # Remove any non-numeric characters except commas
                annual_income_str = ''.join(c for c in annual_income_str 
                                          if c.isdigit() or c == ',')
                if not annual_income_str:
                    logger.warning(f"Skipping occupation {occupation['name']}: Invalid income data")
                    continue
                
                annual_income = float(annual_income_str.replace(',', ''))
                
                # Clean employment data
                employment_str = occupation['total_employment']
                employment_str = ''.join(c for c in employment_str 
                                       if c.isdigit() or c == ',')
                total_employment = int(employment_str.replace(',', ''))
                
                # Calculate income range (±30% of median)
                income_range = [
                    int(annual_income * 0.7),
                    int(annual_income * 1.3)
                ]
                
                # Validate and clean education probabilities
                education_probs = {}
                for level, prob in occupation['education_levels'].items():
                    try:
                        # Convert probability to float and validate
                        prob_value = float(str(prob).replace('%', ''))
                        if 0 <= prob_value <= 100:
                            education_probs[level] = prob_value
                    except (ValueError, TypeError):
                        logger.warning(f"Invalid probability for {level} in {occupation['name']}")
                
                if not education_probs:
                    logger.warning(f"Skipping occupation {occupation['name']}: No valid education data")
                    continue
                
                processed_data[occupation['name']] = {
                    'annual_median_income': annual_income,
                    'valid_income_range': income_range,
                    'education_probabilities': education_probs,
                    'total_employment': total_employment,
                }
                
            except (KeyError, ValueError) as e:
                logger.warning(f"Error processing occupation {occupation.get('name', 'unknown')}: {str(e)}")
                continue
        
        if not processed_data:
            raise ValueError("No valid occupation data could be processed")
        
        logger.info(f"Successfully loaded {len(processed_data)} occupations")
        return processed_data
        
    except Exception as e:
        logger.error(f"Error loading occupation data: {str(e)}")
        raise

def save_population_statistics(personas: List[Persona], output_dir: Path):
    """
    Generate and save comprehensive population statistics as a Markdown file with tables.
    
    Args:
        personas: List of generated Persona objects
        output_dir: Output directory path
    """
    
    def create_md_table(headers: List[str], rows: List[List[Any]]) -> str:
        """Create a markdown table from headers and rows"""
        # Format headers
        header_row = " | ".join(str(h) for h in headers)
        separator = "|".join("---" for _ in headers)
        # Format data rows
        data_rows = [" | ".join(str(cell) for cell in row) for row in rows]
        
        return f"| {header_row} |\n|{separator}|\n" + "\n".join(f"| {row} |" for row in data_rows)

    # Extract raw data from personas
    raw_data = [p.metadata['raw_data'] for p in personas]
    
    # Initialize statistics content
    content = ["# Population Statistics Report\n"]
    content.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    content.append(f"Total Population Size: {len(personas)}\n")
    
    # 1. Demographic Overview
    content.append("## 1. Demographics\n")
    
    # Age Statistics
    ages = [d['age'] for d in raw_data]
    age_ranges = {
        '18-25': len([a for a in ages if 18 <= a <= 25]),
        '26-35': len([a for a in ages if 26 <= a <= 35]),
        '36-50': len([a for a in ages if 36 <= a <= 50]),
        '51-65': len([a for a in ages if 51 <= a <= 65]),
        '65+': len([a for a in ages if a > 65])
    }
    
    content.append("### Age Distribution\n")
    age_rows = [[range_name, count, f"{(count/len(ages))*100:.1f}%"] 
                for range_name, count in age_ranges.items()]
    content.append(create_md_table(["Age Range", "Count", "Percentage"], age_rows))
    content.append(f"\nMean Age: {np.mean(ages):.1f}")
    content.append(f"\nMedian Age: {np.median(ages):.1f}\n")
    
    # Gender Distribution
    content.append("\n### Gender Distribution\n")
    gender_counts = Counter(d['gender'] for d in raw_data)
    gender_rows = [[gender, count, f"{(count/len(raw_data))*100:.1f}%"] 
                   for gender, count in gender_counts.items()]
    content.append(create_md_table(["Gender", "Count", "Percentage"], gender_rows))
    
    # 2. Education and Occupation
    content.append("\n## 2. Education and Employment\n")
    
    # Education Distribution
    content.append("### Education Levels\n")
    edu_counts = Counter(d['education_level'] for d in raw_data)
    edu_rows = [[level, count, f"{(count/len(raw_data))*100:.1f}%"] 
                for level, count in edu_counts.most_common()]
    content.append(create_md_table(["Education Level", "Count", "Percentage"], edu_rows))
    
    # Occupation Distribution
    content.append("\n### Occupations\n")
    occ_counts = Counter(d['occupation'] for d in raw_data)
    occ_rows = [[occ, count, f"{(count/len(raw_data))*100:.1f}%"] 
                for occ, count in occ_counts.most_common()]
    content.append(create_md_table(["Occupation", "Count", "Percentage"], occ_rows))
    
    # 3. Income Analysis
    content.append("\n## 3. Income Analysis\n")
    incomes = [d['income'] for d in raw_data]
    
    # Income brackets
    income_brackets = [
        ('< $30k', lambda x: x < 30000),
        ('$30k - $50k', lambda x: 30000 <= x < 50000),
        ('$50k - $75k', lambda x: 50000 <= x < 75000),
        ('$75k - $100k', lambda x: 75000 <= x < 100000),
        ('$100k - $150k', lambda x: 100000 <= x < 150000),
        ('$150k+', lambda x: x >= 150000)
    ]
    
    income_dist = {
        bracket: len([i for i in incomes if condition(i)])
        for bracket, condition in income_brackets
    }
    
    income_rows = [[bracket, count, f"{(count/len(incomes))*100:.1f}%"] 
                   for bracket, count in income_dist.items()]
    content.append(create_md_table(["Income Bracket", "Count", "Percentage"], income_rows))
    
    content.append(f"\nMean Income: ${np.mean(incomes):,.2f}")
    content.append(f"\nMedian Income: ${np.median(incomes):,.2f}")
    
    # 4. Personality Traits Analysis
    content.append("\n## 4. Personality Traits\n")
    
    traits = ['openness', 'conscientiousness', 'extraversion', 'agreeableness', 'neuroticism']
    trait_stats = []
    
    for trait in traits:
        values = [d[trait] for d in raw_data]
        trait_stats.append([
            trait.capitalize(),
            f"{np.mean(values):.2f}",
            f"{np.median(values):.2f}",
            f"{np.std(values):.2f}",
            f"{np.min(values):.2f}",
            f"{np.max(values):.2f}"
        ])
    
    content.append(create_md_table(
        ["Trait", "Mean", "Median", "Std Dev", "Min", "Max"],
        trait_stats
    ))
    
    # 5. Cross-tabulation Analysis
    content.append("\n## 5. Cross-tabulation Analysis\n")
    
    # Education vs Income
    content.append("\n### Education Level vs. Mean Income\n")
    edu_income = defaultdict(list)
    for d in raw_data:
        edu_income[d['education_level']].append(d['income'])
    
    edu_income_rows = [
        [edu, f"${np.mean(incomes):,.2f}", len(incomes)]
        for edu, incomes in edu_income.items()
    ]
    content.append(create_md_table(
        ["Education Level", "Mean Income", "Sample Size"],
        sorted(edu_income_rows, key=lambda x: x[1], reverse=True)
    ))
    
    # Age Groups vs Occupation
    content.append("\n### Age Groups vs Top Occupations\n")
    age_groups = {
        '18-35': lambda x: 18 <= x <= 35,
        '36-50': lambda x: 36 <= x <= 50,
        '51+': lambda x: x > 50
    }
    
    top_occupations = [occ for occ, _ in occ_counts.most_common(5)]
    age_occ_matrix = []
    
    for age_group, age_filter in age_groups.items():
        age_filtered = [d for d in raw_data if age_filter(d['age'])]
        total_in_group = len(age_filtered)
        if total_in_group == 0:
            continue
            
        occ_in_group = Counter(d['occupation'] for d in age_filtered)
        row = [age_group]
        for occ in top_occupations:
            percentage = (occ_in_group[occ] / total_in_group) * 100
            row.append(f"{percentage:.1f}%")
        row.append(str(total_in_group))
        age_occ_matrix.append(row)
    
    headers = ["Age Group"] + top_occupations + ["Total"]
    content.append(create_md_table(headers, age_occ_matrix))
    
    # 6. Personality Traits by Generation
    content.append("\n## 6. Personality Traits by Generation\n")
    
    # Update generations definition to handle all possible ages
    generations = {
        '18-25': lambda x: 18 <= x <= 25,
        '26-40': lambda x: 26 <= x <= 40,
        '41-55': lambda x: 41 <= x <= 55,
        '56+': lambda x: x >= 56  # This catches all older ages
    }
    
    gen_traits = []
    for gen_name, gen_filter in generations.items():
        gen_data = [d for d in raw_data if gen_filter(d['age'])]
        if not gen_data:  # Skip empty generations but log it
            logger.warning(f"No data found for generation: {gen_name}")
            continue
            
        row = [gen_name]
        for trait in traits:
            trait_vals = [d[trait] for d in gen_data]
            row.append(f"{np.mean(trait_vals):.2f}")
        row.append(len(gen_data))  # Add sample size
        gen_traits.append(row)
    
    # Add total population stats
    total_row = ["Total Population"]
    for trait in traits:
        all_vals = [d[trait] for d in raw_data]
        total_row.append(f"{np.mean(all_vals):.2f}")
    total_row.append(len(raw_data))
    gen_traits.append(total_row)
    
    content.append(create_md_table(
        ["Generation"] + [t.capitalize() for t in traits] + ["Sample Size"],
        gen_traits
    ))
    
    # Add DTS Statistics section if available
    wandering_stats = any('wandering_iteration' in p.metadata.get('raw_data', {}).get('metadata', {}) 
                     for p in personas)
    
    if wandering_stats:
        content.append("\n## 7. DTS Generation Statistics\n")
        
        # Get DTS metadata from personas
        wandering_metadata = [p.metadata['raw_data']['metadata'] for p in personas 
                        if 'metadata' in p.metadata['raw_data']]
        
        # Basic DTS Statistics
        content.append("### Basic DTS Metrics\n")
        
        # Calculate acceptance rate
        acceptance_rates = [m.get('acceptance_rate', 0) for m in wandering_metadata]
        mean_acceptance = np.mean(acceptance_rates)
        
        # Calculate fitness scores
        fitness_scores = [m.get('fitness_score', 0) for m in wandering_metadata]
        
        wandering_basic_stats = [
            ["Mean Acceptance Rate", f"{mean_acceptance:.2%}"],
            ["Mean fitness Score", f"{np.mean(fitness_scores):.3f}"],
            ["Median fitness Score", f"{np.median(fitness_scores):.3f}"],
            ["Min fitness Score", f"{np.min(fitness_scores):.3f}"],
            ["Max fitness Score", f"{np.max(fitness_scores):.3f}"]
        ]
        
        content.append(create_md_table(
            ["Metric", "Value"],
            wandering_basic_stats
        ))
        
        # fitness Score Distribution
        content.append("\n### fitness Score Distribution\n")
        
        # Create fitness score brackets
        min_score = np.min(fitness_scores)
        max_score = np.max(fitness_scores)
        score_range = max_score - min_score
        num_brackets = 5
        bracket_size = score_range / num_brackets
        
        fitness_brackets = []
        for i in range(num_brackets):
            lower = min_score + (i * bracket_size)
            upper = min_score + ((i + 1) * bracket_size)
            count = len([s for s in fitness_scores if lower <= s < upper])
            fitness_brackets.append([
                f"{lower:.3f} - {upper:.3f}",
                count,
                f"{(count/len(fitness_scores))*100:.1f}%"
            ])
        
        content.append(create_md_table(
            ["Score Range", "Count", "Percentage"],
            fitness_brackets
        ))
        
        # Chain Progression Analysis
        content.append("\n### Chain Progression Analysis\n")
        
        # Group personas by DTS iteration ranges
        iterations = [m.get('wandering_iteration', 0) for m in wandering_metadata]
        max_iter = max(iterations)
        iter_ranges = [
            (0, max_iter//4),
            (max_iter//4, max_iter//2),
            (max_iter//2, 3*max_iter//4),
            (3*max_iter//4, max_iter)
        ]
        
        chain_progression = []
        for start, end in iter_ranges:
            range_personas = [p for p, m in zip(personas, wandering_metadata) 
                            if start <= m.get('wandering_iteration', 0) < end]
            if not range_personas:
                continue
                
            range_scores = [m.get('fitness_score', 0) for m in wandering_metadata 
                          if start <= m.get('wandering_iteration', 0) < end]
            
            chain_progression.append([
                f"Iterations {start}-{end}",
                len(range_personas),
                f"{np.mean(range_scores):.3f}",
                f"{np.std(range_scores):.3f}"
            ])
        
        content.append(create_md_table(
            ["Iteration Range", "Sample Size", "Mean fitness", "Std Dev"],
            chain_progression
        ))
        
        # Add correlation analysis between fitness and key attributes
        content.append("\n### Correlation with Key Attributes\n")
        
        correlations = []
        numeric_attributes = ['age', 'income'] + traits
        
        for attr in numeric_attributes:
            values = [float(d[attr]) for d in raw_data]
            correlation = np.corrcoef(values, fitness_scores)[0,1]
            correlations.append([
                attr.capitalize(),
                f"{correlation:.3f}"
            ])
        
        content.append(create_md_table(
            ["Attribute", "Correlation with fitness"],
            sorted(correlations, key=lambda x: abs(float(x[1])), reverse=True)
        ))

    # Save the report
    output_path = output_dir / "population_statistics.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))
    
    logger.info(f"Population statistics saved to {output_path}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate personas using DTS or basic generation')
    
    # Add arguments
    parser.add_argument('--no-wandering', action='store_true',
                       help='Disable DTS and use basic generation')
    parser.add_argument('--num-personas', type=int, default=100,
                       help='Number of personas to generate (default: 100)')
    parser.add_argument('--iterations', type=int, default=1000,
                       help='Number of DTS iterations (default: 1000)')
    parser.add_argument('--burn-in', type=int, default=100,
                       help='Number of burn-in iterations (default: 100)')
    parser.add_argument('--exploration-rate', type=float, default=0.1,
                       help='exploration rate (default: 0.1)')
    parser.add_argument('--output-dir', type=str, default='output',
                       help='Output directory (default: output)')
    parser.add_argument('--debug', action='store_true',
                       help='Enable debug logging')
    parser.add_argument('--skip-visualizations', action='store_true',
                       help='Skip generating visualizations')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Create timestamped output directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_output_dir = Path(args.output_dir) / timestamp
    base_output_dir.mkdir(parents=True, exist_ok=True)
    
    # Configure logging based on debug flag
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    
    try:
        # Load configurations
        logger.info("Loading configuration files...")
        relationships = AttributeRelationships(ATTRIBUTE_RELATIONSHIPS_FILE)
        options = AttributeOptions(ATTRIBUTE_OPTIONS_FILE)
        
        # Initialize generators
        base_generator = PersonaGenerator(relationships, options)
        
        if not args.no_wandering:
            logger.info("Initializing DTS generator...")
            wandering_generator = DivergentTreeSampler(
                base_generator,
                num_iterations=args.iterations,
                burn_in=args.burn_in,
                exploration_rate=args.exploration_rate
            )
            
            logger.info("Starting persona generation with DTS")
            personas = wandering_generator.generate_personas(args.num_personas)
            
            if not args.skip_visualizations:
                # Create visualization directories
                visualization_dir = base_output_dir / "visualizations"
                diagnostic_dir = visualization_dir / "diagnostics"
                personality_dir = visualization_dir / "personality"
                
                for dir_path in [diagnostic_dir, personality_dir]:
                    dir_path.mkdir(parents=True, exist_ok=True)
                
                # Generate standard DTS diagnostics
                logger.info("Generating DTS diagnostics visualizations...")
                visualizer = Visualizer(
                    chain_history=wandering_generator.chain_history,
                    acceptance_history=wandering_generator.acceptance_history,
                    burn_in=wandering_generator.burn_in
                )
                visualizer.save_visualization(diagnostic_dir)
                logger.info(f"Saved diagnostic visualizations to {diagnostic_dir}")
                
                # Generate detailed personality analysis
                logger.info("Generating personality trait analysis...")
                personality_fig = visualizer.plot_personality_analysis()
                personality_fig.savefig(
                    personality_dir / 'personality_analysis.png',
                    dpi=300,
                    bbox_inches='tight'
                )
                plt.close(personality_fig)
                logger.info(f"Saved personality analysis to {personality_dir}")
            
            # Output summary statistics
            acceptance_rate = sum(wandering_generator.acceptance_history) / len(wandering_generator.acceptance_history)
            logger.info("\nDTS Summary Statistics:")
            logger.info(f"- Final acceptance rate: {acceptance_rate:.2f}")
            logger.info(f"- Number of iterations: {wandering_generator.num_iterations}")
            logger.info(f"- Burn-in period: {wandering_generator.burn_in}")
            logger.info(f"- Adaptation rate: {wandering_generator.exploration_rate}")
            
            # Calculate and log additional metrics
            unique_states = len({str(state) for state in wandering_generator.chain_history[wandering_generator.burn_in:]})
            logger.info(f"- Unique states explored: {unique_states}")
            logger.info(f"- State space coverage: {unique_states/len(wandering_generator.chain_history[wandering_generator.burn_in:]):.2%}")
            
        else:
            logger.info("Starting persona generation without DTS")
            personas = [base_generator.generate_persona() for _ in range(args.num_personas)]
        
        # Save personas
        output_dir = base_output_dir / "personas"
        output_dir.mkdir(parents=True, exist_ok=True)
        
        logger.info("\nSaving generated personas...")
        for i, persona in enumerate(personas, 1):
            save_persona_to_file(persona, persona.metadata, output_dir)
            if i % 10 == 0:
                logger.info(f"Saved {i}/{len(personas)} personas...")
        
        logger.info("\nGenerating population statistics...")
        stats_dir = base_output_dir / "statistics"
        save_population_statistics(personas, stats_dir)

        logger.info(f"\nSuccessfully completed:")
        logger.info(f"- Generated {len(personas)} unique personas")
        logger.info(f"- Saved to {base_output_dir}")
        if not args.no_wandering and not args.skip_visualizations:
            logger.info(f"- Created visualizations in {visualization_dir}")
        
    except Exception as e:
        logger.error(f"Error in main execution: {e}")
        raise

if __name__ == "__main__":
    main()