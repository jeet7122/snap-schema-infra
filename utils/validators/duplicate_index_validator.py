from models.schema_models import (
    SchemaResponse,
    DeterministicWarning
)


def validate_duplicate_indexes(schema: SchemaResponse):
    warnings = []

    for table in schema.tables:

        sql = table.sql_query.lower()

        for index in table.indexes:

            lower_index = index.lower()

            if "unique index" in lower_index:

                parts = lower_index.split("(")

                if len(parts) < 2:
                    continue

                column = parts[1].replace(")", "").strip()

                if f"{column} " in sql and "unique" in sql:

                    warnings.append(
                        DeterministicWarning(
                            validator="duplicate_index_validator",
                            issue=f"Redundant unique index on {table.table_name}.{column}",
                            recommendation="Remove explicit unique index because UNIQUE constraint already creates backing index."
                        )
                    )

    return warnings