"""
Deterministic validator responsible for detecting redundant
unique index definitions within generated database schemas.

This validator identifies cases where:
- a column already has a UNIQUE constraint
- an additional explicit UNIQUE INDEX is also created

Since most relational databases automatically generate backing indexes
for UNIQUE constraints, explicit duplicate indexes can:
- waste storage
- increase write overhead
- reduce insert/update performance

The validator helps optimize generated schemas by identifying
unnecessary index duplication.

Used by:
- run_validators()
- validation pipeline
- schema optimization workflow
"""

from models.schema_models import (
    SchemaResponse,
    DeterministicWarning
)


def validate_duplicate_indexes(schema: SchemaResponse):
    """
    Detect redundant unique index definitions in generated schemas.

    This validator scans generated SQL definitions and identifies
    duplicate index scenarios where:
    - a UNIQUE constraint already exists
    - an explicit UNIQUE INDEX is additionally created
      for the same column

    Args:
        schema:
            Structured schema response containing generated
            table definitions and indexes.

    Returns:
        list[DeterministicWarning]:
            List of detected redundant index warnings.

    Used by:
        - run_validators()
        - schema validation pipeline

    Notes:
        - Validation is heuristic-based and uses lightweight
          SQL string analysis.
        - Intended to reduce unnecessary index duplication.
        - Assumes database engines automatically create backing
          indexes for UNIQUE constraints.
        - Current implementation focuses on single-column indexes.
    """

    warnings = []

    for table in schema.tables:

        # Normalize SQL for case-insensitive analysis
        sql = table.sql_query.lower()

        for index in table.indexes:

            lower_index = index.lower()

            # ====================================================
            # UNIQUE INDEX Detection
            # ----------------------------------------------------
            # Analyze explicitly created unique indexes to detect
            # potential redundancy with UNIQUE constraints.
            # ====================================================

            if "unique index" in lower_index:

                parts = lower_index.split("(")

                # Skip malformed index definitions
                if len(parts) < 2:
                    continue

                # Extract indexed column name
                column = parts[1].replace(")", "").strip()

                # =================================================
                # Duplicate UNIQUE Constraint Check
                # -------------------------------------------------
                # If the same column already appears with UNIQUE
                # constraint in table SQL, warn about redundancy.
                # =================================================

                if f"{column} " in sql and "unique" in sql:

                    warnings.append(
                        DeterministicWarning(
                            validator="duplicate_index_validator",

                            issue=(
                                f"Redundant unique index on "
                                f"{table.table_name}.{column}"
                            ),

                            recommendation=(
                                "Remove explicit unique index because "
                                "UNIQUE constraint already creates "
                                "backing index."
                            )
                        )
                    )

    # Return all detected redundancy warnings
    return warnings