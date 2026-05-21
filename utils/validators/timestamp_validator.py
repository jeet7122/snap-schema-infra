"""
Deterministic validator responsible for enforcing timestamp
field consistency across generated database schemas.

This validator ensures tables include standard audit fields:
- created_at
- updated_at

Timestamp fields are important for:
- auditing
- record lifecycle tracking
- synchronization workflows
- soft deletion strategies
- operational debugging

The validator generates advisory warnings when timestamp
fields are missing from generated table definitions.

Used by:
- run_validators()
- validation pipeline
- schema quality enforcement workflow
"""

from models.schema_models import (
    SchemaResponse,
    DeterministicWarning
)


def validate_timestamps(
    schema: SchemaResponse
):
    """
    Validate presence of required timestamp audit fields.

    This validator scans generated table SQL definitions and checks
    whether standard audit timestamp fields are present.

    Required Fields:
        - created_at
        - updated_at

    Args:
        schema:
            Structured schema response containing generated
            table definitions.

    Returns:
        list[DeterministicWarning]:
            List of timestamp-related validation warnings.

    Used by:
        - run_validators()
        - schema validation pipeline

    Notes:
        - Validation is deterministic and rule-based.
        - Timestamp enforcement helps maintain audit consistency.
        - Current validation performs lightweight SQL string analysis.
        - Recommendations are advisory unless enforced elsewhere
          in the pipeline.
    """

    warnings = []

    for table in schema.tables:

        # Normalize SQL for case-insensitive analysis
        sql = table.sql_query.lower()

        # ========================================================
        # created_at Validation
        # --------------------------------------------------------
        # Ensure table contains creation timestamp field
        # for auditing and lifecycle tracking.
        # ========================================================

        if "created_at" not in sql:

            warnings.append(
                DeterministicWarning(
                    validator="timestamp_validator",

                    issue=(
                        f"{table.table_name} "
                        f"missing created_at"
                    ),

                    recommendation=(
                        "Add created_at timestamp."
                    )
                )
            )

        # ========================================================
        # updated_at Validation
        # --------------------------------------------------------
        # Ensure table contains update timestamp field
        # for modification tracking.
        # ========================================================

        if "updated_at" not in sql:

            warnings.append(
                DeterministicWarning(
                    validator="timestamp_validator",

                    issue=(
                        f"{table.table_name} "
                        f"missing updated_at"
                    ),

                    recommendation=(
                        "Add updated_at timestamp."
                    )
                )
            )

    # Return all timestamp validation warnings
    return warnings