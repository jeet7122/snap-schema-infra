"""
Deterministic validator responsible for ensuring foreign key
columns are properly indexed within generated database schemas.

Foreign key indexes are critical for:
- JOIN performance
- referential integrity checks
- cascading operations
- query optimization

This validator performs lightweight SQL analysis to detect:
- foreign key UUID columns
- missing index definitions for those columns

The validator helps improve database performance and scalability
by identifying unindexed relationship fields.

Used by:
- run_validators()
- validation pipeline
- schema optimization workflow
"""

import re

from models.schema_models import (
    SchemaResponse,
    DeterministicWarning
)


def validate_foreign_key_indexes(
    schema: SchemaResponse
):
    """
    Detect missing indexes on foreign key columns.

    This validator scans generated table SQL definitions and identifies
    foreign key UUID columns that do not appear to have supporting indexes.

    Foreign key indexing is important for:
        - JOIN efficiency
        - relationship traversal performance
        - cascading DELETE/UPDATE operations
        - query optimization

    Args:
        schema:
            Structured schema response containing generated
            table definitions and indexes.

    Returns:
        list[DeterministicWarning]:
            List of warnings for foreign key columns missing indexes.

    Used by:
        - run_validators()
        - schema validation pipeline

    Notes:
        - Validation uses regex-based SQL parsing.
        - Current implementation focuses on UUID foreign keys.
        - Detection is heuristic-based and may not cover
          all SQL syntax variations.
        - Future versions may support:
            - composite foreign keys
            - partial indexes
            - advanced SQL dialect parsing
    """

    warnings = []

    for table in schema.tables:

        # Normalize SQL for case-insensitive analysis
        sql = table.sql_query.lower()

        # ========================================================
        # Foreign Key Extraction
        # --------------------------------------------------------
        # Extract UUID columns that contain REFERENCES clauses,
        # indicating foreign key relationships.
        # ========================================================

        foreign_keys = re.findall(
            r'(\w+)\s+uuid\s+.*references',
            sql
        )

        # Combine all table indexes into single searchable string
        indexes = " ".join(
            table.indexes
        ).lower()

        for fk in foreign_keys:

            # ====================================================
            # Foreign Key Index Validation
            # ----------------------------------------------------
            # Detect foreign key columns that do not appear in
            # generated index definitions.
            # ====================================================

            if fk not in indexes:

                warnings.append(
                    DeterministicWarning(
                        validator="foreign_key_validator",

                        issue=(
                            f"{table.table_name}.{fk} "
                            f"missing index"
                        ),

                        recommendation=(
                            f"Add index for foreign key "
                            f"column {fk}."
                        )
                    )
                )

    # Return all detected foreign key index warnings
    return warnings