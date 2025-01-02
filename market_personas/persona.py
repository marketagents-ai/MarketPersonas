from pydantic import BaseModel
from typing import List, Optional
import yaml
from pathlib import Path

class Persona(BaseModel):
    """
    A minimal persona model:
      - `name`, `role` for identifying the agent
      - `persona` as a free-form string (or a multi-line YAML block)
      - `objectives` as an optional list of strings
    """
    name: str
    role: str
    persona: str
    objectives: Optional[List[str]] = None  # Now optional with a default of None

def load_persona_from_file(file_path: Path) -> Persona:
    """
    Loads a Persona from a given YAML file path.
    """
    with file_path.open('r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return Persona(**data)

def main():
    # Example 1: Load a generic base persona (may or may not have objectives)
    base_persona_path = Path('persona_template.yaml')
    base_persona = load_persona_from_file(base_persona_path)
    print("Base Persona loaded from template:")
    print(base_persona, "\n")

    # Example 2: Load TARS persona (may or may not have objectives)
    tars_persona_path = Path('examples/tars.yaml')
    tars_persona = load_persona_from_file(tars_persona_path)
    print("TARS Persona loaded:")
    print(tars_persona, "\n")

if __name__ == "__main__":
    main()
