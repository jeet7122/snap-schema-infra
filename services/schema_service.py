"""
Core schema orchestration service responsible for coordinating the
complete AI-driven database schema generation pipeline.

This service acts as the central workflow controller that connects:
- requirement analysis
- relationship planning
- schema generation
- deterministic validation
- architecture review
- SQL compilation
- metadata generation

Pipeline Overview:
1. Analyze natural language requirements
2. Extract entities and features
3. Generate entity relationships
4. Generate database schema
5. Perform schema validation
6. Run deterministic validators
7. Generate auto-fix recommendations
8. Perform AI architecture review
9. Compile SQL output
10. Build schema metadata

The final response returned by this service represents the fully
processed and validated schema generation result.

Used by:
- API Controllers
- Schema Generation Endpoints
- Frontend Clients
"""

from agents.schema_agent import generate_schema
from agents.requirements_analysis_agent import analyze_requirements
from agents.relationship_agent import generate_relationships
from agents.review_agent import review_architecture

from models.schema_models import SchemaResponse

from utils.schema_validator import validate_schema
from utils.run_validators import run_validators
from utils.autofix_engine import generate_auto_fixes
from utils.sql_compiler import compile_sql
from utils.metadata_builder import build_metadata


def generate_schema_service(user_input: str):
    """
    Execute the complete AI-driven schema generation workflow.

    This service orchestrates all agents, validators, and utility
    components required to transform natural language requirements
    into a validated and production-ready database schema response.

    Workflow:
        1. Requirement Analysis
        2. Relationship Planning
        3. Schema Generation
        4. Schema Validation
        5. Deterministic Validation
        6. Auto-Fix Generation
        7. AI Architecture Review
        8. SQL Compilation
        9. Metadata Generation

    Args:
        user_input:
            Natural language application requirements provided by the user.

    Returns:
        dict:
            Fully processed schema response containing:
            - generated tables
            - compiled SQL
            - metadata
            - validation warnings
            - architecture review
            - auto-fix recommendations

    Raises:
        ValidationError:
            Raised when generated schema fails structural validation.

        RuntimeError:
            Raised when any downstream AI agent or utility fails.

    Used by:
        - API Controllers
        - Schema Generation Routes

    Notes:
        - This service acts as the primary orchestration layer.
        - Schema validation occurs before compilation.
        - Deterministic validators provide rule-based safety checks.
        - Auto-fix engine generates SQL repair suggestions.
        - Architecture review is AI-generated and advisory in nature.
    """

    # ============================================================
    # STEP 1: Requirement Analysis
    # ------------------------------------------------------------
    # Extract entities and application features from raw
    # natural language requirements.
    # ============================================================

    requirements = analyze_requirements(user_input)

    entities = requirements["entities"]
    features = requirements["features"]

    # ============================================================
    # STEP 2: Relationship Planning
    # ------------------------------------------------------------
    # Infer entity relationships based on extracted entities
    # and application feature interactions.
    # ============================================================

    relationship_plan = generate_relationships(
        entities=entities,
        features=features
    )

    relationships = relationship_plan["relationships"]

    # ============================================================
    # STEP 3: Schema Generation
    # ------------------------------------------------------------
    # Generate structured database schema using entities,
    # features, and inferred relationships.
    # ============================================================

    schema_result = generate_schema(
        entities,
        features,
        relationships
    )

    # ============================================================
    # STEP 4: Schema Validation
    # ------------------------------------------------------------
    # Validate generated schema structure using Pydantic
    # schema enforcement and custom validation logic.
    # ============================================================

    schema = SchemaResponse(**schema_result)

    validate_schema(schema)

    # ============================================================
    # STEP 5: Deterministic Validation
    # ------------------------------------------------------------
    # Execute rule-based validators to detect schema design
    # issues not covered by AI generation alone.
    # ============================================================

    deterministic_warnings = run_validators(schema)

    schema.deterministic_warnings = deterministic_warnings

    # ============================================================
    # STEP 6: Auto-Fix Generation
    # ------------------------------------------------------------
    # Generate SQL repair suggestions for warnings identified
    # during deterministic validation.
    # ============================================================

    auto_fixes = generate_auto_fixes(
        schema=schema,
        warnings=deterministic_warnings
    )

    schema.autofixes = auto_fixes

    # ============================================================
    # STEP 7: AI Architecture Review
    # ------------------------------------------------------------
    # Perform AI-driven architecture review to provide
    # scalability and schema design recommendations.
    # ============================================================

    review = review_architecture(schema.model_dump())

    schema.architecture_review = review

    # ============================================================
    # STEP 8: SQL Compilation
    # ------------------------------------------------------------
    # Combine generated table SQL into a single executable
    # compiled SQL output.
    # ============================================================

    schema.compiled_sql = compile_sql(schema)

    # ============================================================
    # STEP 9: Metadata Generation
    # ------------------------------------------------------------
    # Build aggregated metadata such as total tables
    # and generated indexes.
    # ============================================================

    schema.metadata = build_metadata(schema)

    # Return fully processed schema response
    return schema.model_dump()