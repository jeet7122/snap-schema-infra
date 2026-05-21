"""
SQL compilation utility responsible for generating a unified
SQL script from structured schema output.

This utility aggregates:
- table creation queries
- index creation statements

into a single executable SQL output string.

The compiled SQL is later returned in the final API response
and can be directly executed against supported databases.

Used by:
- schema_service
- SQL export pipeline
- Database deployment workflows
"""

from models.schema_models import SchemaResponse


def compile_sql(schema: SchemaResponse):
    """
    Compile generated schema objects into a single SQL script.

    This method iterates through all generated tables and combines:
    - CREATE TABLE statements
    - index creation queries

    into a properly formatted executable SQL output.

    Args:
        schema:
            Structured schema response containing generated
            table definitions and indexes.

    Returns:
        str:
            Combined SQL script containing all table and
            index creation statements.

    Used by:
        - generate_schema_service()

    Notes:
        - SQL statements are separated using double line breaks
          for improved readability.
        - Index queries are appended immediately after their
          corresponding table definition.
        - Compilation assumes table SQL has already been validated.
    """

    sql_parts = []

    for table in schema.tables:

        # Append CREATE TABLE query
        sql_parts.append(table.sql_query)

        # Append associated index creation queries
        sql_parts.extend(table.indexes)

    # Combine all SQL statements into single executable script
    return "\n\n".join(sql_parts)