from agents.schema_agent import generate_schema
from models.schema_models import SchemaResponse
from utils.schema_validator import validate_schema

def generate_schema_service(user_input: str):
    result = generate_schema(user_input)
    validated = SchemaResponse(**result)
    validate_schema(validated)
    return validated.model_dump()