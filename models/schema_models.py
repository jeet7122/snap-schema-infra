from pydantic import BaseModel
from typing import List

"""
Model for holding extra fields/suggestion from LLM
"""

class ExtraField(BaseModel):
    columnName: str
    reason: str

"""
Model for holding TableSchema from LLM
"""

class TableSchema(BaseModel):
    table_name: str
    sql_query: str
    indexes: List[str]
    extras: List[str]
    
"""
API Response Model for users
"""
class SchemaResponse(BaseModel):
    tables: List[TableSchema]
   
    
"""
API Request Model for users
"""    
class SchemaRequest(BaseModel):
    user_input: str
    
    