from models.schema_models import SchemaResponse

def compile_sql(schema: SchemaResponse):
    sql_parts = []
    
    for table in schema.tables:
        sql_parts.append(table.sql_query)
        sql_parts.extend(table.indexes)
        
    return "\n\n".join(sql_parts)
