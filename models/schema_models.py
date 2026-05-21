from pydantic import BaseModel
from typing import List


class AutoFix(BaseModel):
    issue: str
    fix_sql: str


class AutoFixReport(BaseModel):
    fixes: list[AutoFix]

    
    

class DeterministicWarning(BaseModel):
    validator: str
    issue: str
    recommendation: str


class ValidationReport(BaseModel):
    warnings: list[DeterministicWarning]



"""
Model for holding metadata about output from LLM
"""

class MetaData(BaseModel):
    total_tables: int
    total_indexes: int

"""
Model for holding extra fields/suggestion from LLM
"""

class ExtraField(BaseModel):
    columnName: str
    reason: str
    
class ArchitectWarning(BaseModel):
    issue: str
    recommendation: str

class ArchitectureReview(BaseModel):
    warnings: list[ArchitectWarning]


"""
Model for holding TableSchema from LLM
"""
class TableSchema(BaseModel):
    table_name: str
    sql_query: str
    indexes: List[str]
    extras: List[ExtraField]
    
"""
API Response Model for users
"""
class SchemaResponse(BaseModel):
    tables: List[TableSchema]
    compiled_sql: str | None = None
    metadata: MetaData | None = None
    architecture_review: ArchitectureReview | None = None
    deterministic_warnings: list[DeterministicWarning] | None = None
    autofixes: list[AutoFix] | None = None
   
    
"""
API Request Model for users
"""    
class SchemaRequest(BaseModel):
    user_input: str
    

"""
Requirement Analysis Model for gathering requirements for structured result
"""   
class RequirementAnalysis(BaseModel):
    entities: list[str]
    features: list[str]
    
class RelationShip(BaseModel):
    source: str
    target: str
    relationship_type: str
    foreign_key: str

class RelationShipPlan(BaseModel):
    relationships: list[RelationShip]
    
    
