from core.llm import llm
from prompts.generate_sql_prompt import generate_sql_query_prompt
from models.schema_models import SchemaResponse, RelationShip

structured_llm = llm.with_structured_output(SchemaResponse)



def generate_schema(entities: list[str], features: list[str], relationships: list[RelationShip]):
    prompt = generate_sql_query_prompt.format(entities=entities, features=features, relationships=relationships)
    response = structured_llm.invoke(prompt)
    return response.model_dump()
    