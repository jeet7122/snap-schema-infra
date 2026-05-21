"""
Deterministic validator responsible for detecting potential
enum-style lookup tables within generated database schemas.

This validator identifies tables whose names suggest they may represent:
- statuses
- roles
- categories
- permissions
- fixed-type definitions

In many cases, such tables can alternatively be modeled using:
- ENUM fields
- CHECK constraints
- constrained value sets

The validator provides architecture-level recommendations to help
optimize schema simplicity and reduce unnecessary table fragmentation.

Used by:
- run_validators()
- validation pipeline
- schema optimization workflow
"""

from models.schema_models import (
    SchemaResponse,
    DeterministicWarning
)


# ================================================================
# Keywords commonly associated with enum-style lookup tables.
# ---------------------------------------------------------------
# These are heuristic indicators only and do not guarantee
# improper normalization.
# ================================================================

ENUM_TABLE_KEYWORDS = [
    "status",
    "role",
    "type",
    "category",
    "permission"
]


def validate_enum_modeling(
    schema: SchemaResponse
):
    """
    Detect potential enum-style lookup tables in generated schemas.

    This validator performs heuristic analysis on generated table names
    to identify tables that may represent finite/static value sets.

    Potential alternatives may include:
        - ENUM fields
        - CHECK constraints
        - application-level enums

    Args:
        schema:
            Structured schema response containing generated
            database table definitions.

    Returns:
        list[DeterministicWarning]:
            List of schema modeling recommendations related
            to enum-style table detection.

    Used by:
        - run_validators()
        - schema validation pipeline

    Notes:
        - Detection is keyword-based and heuristic-driven.
        - Recommendations are advisory only.
        - Lookup tables may still be appropriate depending on:
            - extensibility requirements
            - localization needs
            - relational complexity
            - admin configurability
    """

    warnings = []

    for table in schema.tables:

        # Normalize table name for case-insensitive analysis
        table_name = table.table_name.lower()

        for keyword in ENUM_TABLE_KEYWORDS:

            # ====================================================
            # Enum-Style Table Detection
            # ----------------------------------------------------
            # Detect table names that resemble static lookup
            # or finite-value enum structures.
            # ====================================================

            if keyword in table_name:

                warnings.append(
                    DeterministicWarning(
                        validator="enum_validator",

                        issue=(
                            f"Potential enum-style table detected: "
                            f"{table.table_name}"
                        ),

                        recommendation=(
                            "Consider replacing with CHECK constraint "
                            "or ENUM field."
                        )
                    )
                )

    # Return all enum modeling recommendations
    return warnings