"""
Metadata builder utility responsible for generating aggregated
schema statistics from the generated database schema output.

This utility extracts high-level schema metrics used for:
- API response enrichment
- schema analytics
- reporting
- quick structural summaries

Currently generated metadata includes:
- total generated tables
- total generated indexes

Used by:
- schema_service
- API response layer
- schema analytics pipeline
"""

from models.schema_models import (
    SchemaResponse,
    MetaData
)


def build_metadata(schema: SchemaResponse):
    """
    Generate aggregated metadata for the generated schema.

    This method analyzes the generated schema and computes
    high-level structural statistics used in the final API response.

    Args:
        schema:
            Structured schema response containing generated
            tables and index definitions.

    Returns:
        MetaData:
            Aggregated schema metadata containing:
            - total tables
            - total indexes

    Used by:
        - generate_schema_service()

    Notes:
        - Metadata generation occurs after schema validation
          and SQL compilation.
        - Index count is calculated dynamically across all tables.
        - Designed to support future schema analytics expansion.
    """

    # Calculate total number of generated indexes
    total_indexes = sum(
        len(table.indexes)
        for table in schema.tables
    )

    # Build and return aggregated schema metadata
    return MetaData(
        total_tables=len(schema.tables),
        total_indexes=total_indexes
    )