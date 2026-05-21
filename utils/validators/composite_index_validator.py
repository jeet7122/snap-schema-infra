from models.schema_models import (
    SchemaResponse,
    DeterministicWarning
)


def validate_composite_indexes(
    schema: SchemaResponse
):

    warnings = []

    for table in schema.tables:

        sql = table.sql_query.lower()

        if "status" in sql:

            warnings.append(
                DeterministicWarning(
                    validator="composite_index_validator",
                    issue=f"{table.table_name} may benefit from composite indexes",
                    recommendation=f"Consider indexes like ({table.table_name}_id, status)."
                )
            )

    return warnings