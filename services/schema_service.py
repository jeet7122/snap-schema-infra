from agents.schema_agent import generate_schema
from agents.requirements_analysis_agent import analyze_requirements
from agents.relationship_agent import generate_relationships
from agents.review_agent import review_architecture
from models.schema_models import SchemaResponse
from utils.schema_validator import validate_schema
from utils.run_validators import run_validators
from utils.sql_compiler import compile_sql
from utils.metadata_builder import build_metadata

def generate_schema_service(user_input: str):
    # STEP 1: Analyze Requirements
    requirements = analyze_requirements(user_input)
    entities = requirements["entities"]
    features = requirements["features"]
    
    #STEP 2: Relationship Planning
    relationship_plan = generate_relationships(
        entities=entities, features=features
    )
    relationships = relationship_plan["relationships"]
    
    # STEP 3: Schema Genaration
    schema_result = generate_schema(entities, features, relationships)
    
    # STEP 4: Validation
    schema = SchemaResponse(**schema_result)
    validate_schema(schema)
    
    # STEP 5: Determinitic Validators
    deterministic_warnings = run_validators(schema)
    schema.deterministic_warnings = deterministic_warnings
    
    # STEP 6: AI Review Architecture
    review = review_architecture(schema.model_dump())
    schema.architecture_review = review
    
    # STEP 7: SQL Compilation
    schema.compiled_sql = compile_sql(schema)
    
    # STEP 8: Metadata Generation
    schema.metadata = build_metadata(schema)
    
    return schema.model_dump()