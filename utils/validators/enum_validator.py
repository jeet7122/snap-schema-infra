from models.schema_models import (
    SchemaResponse,
    DeterministicWarning
)


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

    warnings = []

    for table in schema.tables:

        table_name = table.table_name.lower()

        for keyword in ENUM_TABLE_KEYWORDS:

            if keyword in table_name:

                warnings.append(
                    DeterministicWarning(
                        validator="enum_validator",
                        issue=f"Potential enum-style table detected: {table.table_name}",
                        recommendation="Consider replacing with CHECK constraint or ENUM field."
                    )
                )

    return warnings