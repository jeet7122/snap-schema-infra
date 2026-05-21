from models.schema_models import (
    SchemaResponse,
    AutoFix
)


def generate_auto_fixes(
    schema: SchemaResponse,
    warnings
):

    fixes = []

    for warning in warnings:

        validator = warning.validator

        # FK INDEX FIX
        if validator == "foreign_key_validator":

            issue = warning.issue

            try:

                parts = issue.split(".")

                table_name = parts[0]

                fk_column = (
                    parts[1]
                    .replace(" missing index", "")
                )

                fixes.append(
                    AutoFix(
                        issue=issue,
                        fix_sql=(
                            f"CREATE INDEX "
                            f"idx_{table_name}_{fk_column} "
                            f"ON {table_name}({fk_column});"
                        )
                    )
                )

            except Exception:
                pass

        # TIMESTAMP FIX
        elif validator == "timestamp_validator":

            issue = warning.issue

            if "created_at" in issue:

                table_name = issue.split()[0]

                fixes.append(
                    AutoFix(
                        issue=issue,
                        fix_sql=(
                            f"ALTER TABLE {table_name} "
                            f"ADD COLUMN created_at "
                            f"TIMESTAMP WITH TIME ZONE "
                            f"DEFAULT CURRENT_TIMESTAMP;"
                        )
                    )
                )

            elif "updated_at" in issue:

                table_name = issue.split()[0]

                fixes.append(
                    AutoFix(
                        issue=issue,
                        fix_sql=(
                            f"ALTER TABLE {table_name} "
                            f"ADD COLUMN updated_at "
                            f"TIMESTAMP WITH TIME ZONE "
                            f"DEFAULT CURRENT_TIMESTAMP;"
                        )
                    )
                )

    return fixes