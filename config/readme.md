# Persona Generator YAML Configuration Guide

This guide explains how to configure the persona generation system through its YAML configuration files. The system uses three main configuration files to define attributes, relationships, and output templates.

## Configuration Files Overview

- `attribute_options.yaml`: Defines all possible attributes and their valid values
- `attribute_relationships.yaml`: Defines how attributes influence each other
- `persona_template.yaml`/`.md`: Defines output formatting for generated personas

## 1. Attribute Options Configuration (attribute_options.yaml)

### Basic Structure
Attributes can be defined in two ways:
```yaml
# Range-based attributes
attribute_name:
  range: 'min-max'

# Option-based attributes
attribute_name:
  options:
    - value: option1
      distribution: weight
```

### Range Attributes
Used for numeric values:
```yaml
age:
  range: '18-80'

income:
  range: '20000-300000'

stress_level:
  range: '0-100'
```

### Option Attributes
Used for categorical values:
```yaml
gender:
  options:
    - value: Male
      distribution: 49
    - value: Female
      distribution: 49
    - value: Non-binary
      distribution: 2
```

### Complex Attributes (e.g., Occupations)
For attributes with multiple constraints:
```yaml
occupation:
  options:
    - value: Software Developer
      total_employment: 1656880
      valid_education: [Some College, Bachelor's Degree, Master's Degree]
      valid_income_range: [92589, 171951]
      min_age: 22
      retirement_age: 65
      retirement_exceptions: true
```

## 2. Attribute Relationships Configuration (attribute_relationships.yaml)

### Basic Structure
```yaml
primary_attribute:
  relationships:
    - secondary_attribute: influenced_attribute
      weight: correlation_strength
      conditions: [optional_conditions]
```

### Weight Values
- Positive weights (0 to 1): Positive correlation
- Negative weights (-1 to 0): Negative correlation
- Higher absolute values = stronger relationship

### Example Configuration
```yaml
age:
  relationships:
    - secondary_attribute: education_level
      weight: 0.8
      conditions: [age<22]
    - secondary_attribute: income
      weight: 0.6
      conditions: [age>25]
```

### Conditional Relationships
Conditions can include:
- Age-based conditions: `age>25`, `age<65`
- Value-based conditions: `income>50000`
- Multiple conditions using arrays

## 3. Template Configuration

### YAML Template (persona_template.yaml)
```yaml
template: >
  name: {name}
  demographics:
    age: {age}
    gender: {gender}
    occupation: {occupation}
```

### Markdown Template (persona_template.md)
```markdown
# {name}

## Description
{name} is a {age}-year-old {gender}...

## Demographics
- Age: {age}
- Gender: {gender}
```

## Best Practices

1. Attribute Definitions
   - Always provide valid ranges/options
   - Include distribution weights for options
   - Define clear constraints

2. Relationships
   - Keep weights realistic (-1 to 1)
   - Use conditions to limit scope
   - Consider indirect relationships

3. Validation
   - Check for circular dependencies
   - Verify value ranges
   - Test relationship impacts

## Common Gotchas

1. Distribution Weights
   - Must sum to reasonable proportions
   - Consider real-world distributions

2. Relationship Chains
   - Beware of circular relationships
   - Consider cumulative effects

3. Range Constraints
   - Ensure ranges are realistic
   - Consider edge cases

## Examples

### Adding a New Attribute
```yaml
# In attribute_options.yaml
new_attribute:
  options:
    - value: Option1
      distribution: 40
    - value: Option2
      distribution: 60

# In attribute_relationships.yaml
new_attribute:
  relationships:
    - secondary_attribute: existing_attribute
      weight: 0.5
      conditions: []
```

### Modifying Templates
```yaml
# Add to template files
new_section:
  new_attribute: {new_attribute}
```

## Troubleshooting

1. Invalid Configurations
   - Check value ranges
   - Verify relationship weights
   - Validate distribution sums

2. Performance Issues
   - Reduce relationship complexity
   - Optimize range constraints
   - Simplify condition checks

3. Unrealistic Results
   - Review relationship weights
   - Check distribution values
   - Verify constraint logic

## Contributing

When adding or modifying configurations:
1. Document changes clearly
2. Test with diverse scenarios
3. Validate statistical outcomes
4. Update relevant templates

This configuration system allows for flexible and realistic persona generation while maintaining statistical validity and relationship coherence.
