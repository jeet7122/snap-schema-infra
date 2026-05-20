from core.llm import llm
from prompts.requirement_analysis_prompt import requirement_analysis_prompt
from models.schema_models import RequirementAnalysis

structured_llm = llm.with_structured_output(RequirementAnalysis)

def analyze_requirements(user_input: str):
    prompt = requirement_analysis_prompt.format(input=user_input)
    response = structured_llm.invoke(prompt)
    return response.model_dump()