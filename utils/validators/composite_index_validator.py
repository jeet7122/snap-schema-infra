"""
Deterministic validator responsible for identifying tables that may
benefit from composite database indexes.

This validator performs lightweight rule-based analysis on generated
SQL schema definitions to detect query optimization opportunities.

Current Detection Logic:
- identifies tables containing a `status` column
- recommends composite indexes for commonly filtered query patterns

The validator is advisory only and does not modify the schema directly.

Used by:
- run_validators()
- validation pipeline
- auto-fix recommendation engine
"""

from models.schema_models import (
    SchemaResponse,
    DeterministicWarning
)


def validate_composite_indexes(
    schema: SchemaResponse
):
    """
    Analyze generated schema for potential composite index improvements.

    This validator scans generated table SQL definitions and identifies
    cases where composite indexes may improve query performance.

    Current Rule:
        - If a table contains a `status` field, recommend
          composite indexes involving entity identifiers and status.

    Args:
        schema:
            Structured schema response containing generated
            table definitions.

    Returns:
        list[DeterministicWarning]:
            List of optimization warnings and index recommendations.

    Used by:
        - run_validators()
        - schema validation pipeline

    Notes:
        - Validation is heuristic-based and advisory in nature.
        - Recommendations are intended for query-heavy systems.
        - Future implementations may include:
            - foreign key index checks
            - multi-column filter analysis
            - query-pattern-aware optimization
    """

    warnings = []

    for table in schema.tables:

        # Normalize SQL for case-insensitive analysis
        sql = table.sql_query.lower()

        # ========================================================
        # Composite Index Recommendation Check
        # --------------------------------------------------------
        # Tables containing `status` fields often participate in
        # filtered queries and may benefit from composite indexes.
        # ========================================================

        if "status" in sql:

            warnings.append(
                DeterministicWarning(
                    validator="composite_index_validator",

                    issue=(
                        f"{table.table_name} may benefit "
                        f"from composite indexes"
                    ),

                    recommendation=(
                        f"Consider indexes like "
                        f"({table.table_name}_id, status)."
                    )
                )
            )

    # Return all generated optimization warnings
    return warnings