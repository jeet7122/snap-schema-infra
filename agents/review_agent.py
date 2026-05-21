from core.llm import llm
from prompts.architect_review_prompt import architecture_review_prompt
from models.schema_models import ArchitectureReview

structured_llm = llm.with_structured_output(ArchitectureReview)

def review_architecture(schema: dict):
    prompt = architecture_review_prompt.format(schema=schema)
    response = structured_llm.invoke(prompt)
    return response.model_dump()