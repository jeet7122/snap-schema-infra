"""
API route definitions for schema generation endpoints.

This module exposes REST endpoints responsible for interacting with
the AI-driven schema generation pipeline.

The routes act as the HTTP interface layer between:
- frontend clients
- API consumers
- schema orchestration services

Current Endpoints:
- POST /generate-sql-schema

Used by:
- Frontend Applications
- API Clients
- Internal Platform Integrations
"""

from fastapi import APIRouter

from models.schema_models import (
    SchemaRequest,
    SchemaResponse
)

from services.schema_service import generate_schema_service


# ================================================================
# FastAPI router instance used for schema-related endpoints.
# ================================================================

router = APIRouter()


@router.post(
    "/generate-sql-schema",
    response_model=SchemaResponse
)
async def generate_schema_route(
    request: SchemaRequest
):
    """
    Generate database schema from natural language requirements.

    This endpoint accepts user-provided application requirements
    and executes the complete AI-driven schema generation pipeline.

    Pipeline Includes:
        - requirement analysis
        - relationship planning
        - schema generation
        - deterministic validation
        - auto-fix generation
        - architecture review
        - SQL compilation
        - metadata generation

    Request Body:
        SchemaRequest:
            Natural language application requirements.

    Returns:
        SchemaResponse:
            Fully processed schema response containing:
            - generated tables
            - compiled SQL
            - validation warnings
            - architecture review
            - metadata
            - auto-fix recommendations

    Route:
        POST /generate-sql-schema

    Used by:
        - Frontend schema generators
        - API consumers
        - internal automation systems

    Notes:
        - Endpoint uses async FastAPI route handling.
        - Core schema processing is delegated to
          `generate_schema_service()`.
        - Response validation is enforced using Pydantic models.
    """

    # Execute schema generation orchestration pipeline
    result = generate_schema_service(
        request.user_input
    )

    return result