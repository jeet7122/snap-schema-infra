from models.schema_models import SchemaResponse


def validate_schema(schema: SchemaResponse):
    table_names = set()
    
    for table in schema.tables:
        if table.table_name in table_names:
            raise ValueError(f"Duplicate table name: {table.table_name}")
        table_names.add(table.table_name)
        
        if "PRIMARY KEY" not in table.sql_query:
            raise ValueError(f"{table.table_name} missing PRIMARY KEY")
    return schema
