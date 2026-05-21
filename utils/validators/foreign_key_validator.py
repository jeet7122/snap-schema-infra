import re

from models.schema_models import (
    SchemaResponse,
    DeterministicWarning
)


def validate_foreign_key_indexes(
    schema: SchemaResponse
):

    warnings = []

    for table in schema.tables:

        sql = table.sql_query.lower()

        foreign_keys = re.findall(
            r'(\w+)\s+uuid\s+.*references',
            sql
        )

        indexes = " ".join(
            table.indexes
        ).lower()

        for fk in foreign_keys:

            if fk not in indexes:

                warnings.append(
                    DeterministicWarning(
                        validator="foreign_key_validator",
                        issue=f"{table.table_name}.{fk} missing index",
                        recommendation=f"Add index for foreign key column {fk}."
                    )
                )

    return warnings