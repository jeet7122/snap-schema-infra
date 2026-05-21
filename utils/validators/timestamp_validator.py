from models.schema_models import (
    SchemaResponse,
    DeterministicWarning
)


def validate_timestamps(
    schema: SchemaResponse
):

    warnings = []

    for table in schema.tables:

        sql = table.sql_query.lower()

        if "created_at" not in sql:

            warnings.append(
                DeterministicWarning(
                    validator="timestamp_validator",
                    issue=f"{table.table_name} missing created_at",
                    recommendation="Add created_at timestamp."
                )
            )

        if "updated_at" not in sql:

            warnings.append(
                DeterministicWarning(
                    validator="timestamp_validator",
                    issue=f"{table.table_name} missing updated_at",
                    recommendation="Add updated_at timestamp."
                )
            )

    return warnings