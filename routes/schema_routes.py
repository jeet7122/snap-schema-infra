from fastapi import APIRouter
from models.schema_models import (SchemaRequest, SchemaResponse)
from services.schema_service import generate_schema_service

router = APIRouter()


@router.post("/generate-sql-schema", response_model=SchemaResponse)
async def generate_schema_route(request: SchemaRequest):
    result = generate_schema_service(request.user_input)
    return result