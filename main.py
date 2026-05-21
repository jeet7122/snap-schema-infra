"""
Application entry point for the AI-driven schema generation platform.

This module initializes the FastAPI application instance and
registers all API route modules.

Responsibilities:
- initialize FastAPI application
- register API routers
- configure application routing

Application Architecture:
- FastAPI-based REST API
- modular route registration
- AI-driven schema orchestration backend

Used by:
- ASGI servers
- application startup process
- deployment environments
"""

from fastapi import FastAPI

from routes.schema_routes import router


# ================================================================
# Main FastAPI application instance.
# ================================================================

app = FastAPI()


# ================================================================
# Register schema-related API routes.
# ---------------------------------------------------------------
# All endpoints defined in `schema_routes` become available
# through the main application instance.
# ================================================================

app.include_router(router)