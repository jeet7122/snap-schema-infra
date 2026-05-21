from utils.validators.duplicate_index_validator import validate_duplicate_indexes
from models.schema_models import SchemaResponse

def run_validators(schema: SchemaResponse):
    warnings = []
    
    warnings.extend(
        validate_duplicate_indexes(schema)
    )
    return warnings