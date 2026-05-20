from core.llm import llm
from prompts.generate_sql_prompt import generate_sql_query_prompt
from models.schema_models import SchemaResponse

structured_llm = llm.with_structured_output(SchemaResponse)



def generate_schema(user_input: str):
    prompt = generate_sql_query_prompt.format(input=user_input)
    content = llm.invoke(prompt)
    response = structured_llm.invoke(prompt)
    return response.model_dump()
