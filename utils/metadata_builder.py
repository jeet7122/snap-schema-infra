from models.schema_models import (SchemaResponse, MetaData)

def build_metadata(schema: SchemaResponse):
    total_indexes = sum(len(table.indexes) for table in schema.tables)
    return MetaData(
        total_tables=len(schema.tables)
        total_indexes=total_indexes
    )