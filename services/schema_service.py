from agents.schema_agent import generate_schema
from models.schema_models import SchemaResponse
from utils.schema_validator import validate_schema
from utils.sql_compiler import compile_sql
from utils.metadata_builder import build_metadata

def generate_schema_service(user_input: str):
    result = generate_schema(user_input)
    schema = SchemaResponse(**result)
    validate_schema(schema)
    schema.compiled_sql = compile_sql(schema)
    schema.metadata = build_metadata(schema)
    return schema.model_dump()