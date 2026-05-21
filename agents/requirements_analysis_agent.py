"""
Requirement analysis agent responsible for extracting structured
system design information from natural language user requirements.

This agent converts raw user input into normalized structured metadata
used throughout the schema generation pipeline.

Extracted information may include:
- entities
- features
- business modules
- domain-specific components

The generated output acts as the foundational layer for:
- relationship generation
- schema generation
- architecture review

Flow:
1. Accept raw user requirements
2. Inject requirements into analysis prompt
3. Invoke structured LLM extraction
4. Return validated structured analysis output
"""

from core.llm import llm
from prompts.requirement_analysis_prompt import requirement_analysis_prompt
from models.schema_models import RequirementAnalysis


# Configure LLM to return validated RequirementAnalysis structure
structured_llm = llm.with_structured_output(RequirementAnalysis)


def analyze_requirements(user_input: str):
    """
    Analyze user requirements and extract structured application metadata.

    This method transforms raw natural language system requirements
    into normalized structured data used by downstream AI agents.

    Args:
        user_input:
            Natural language application requirements provided by the user.

    Returns:
        dict:
            Structured requirement analysis containing extracted
            entities, features, and domain metadata.

    Used by:
        - schema_service.generate_schema_service()

    Notes:
        - Acts as the entry point of the AI schema generation pipeline.
        - Output is validated against the RequirementAnalysis schema.
        - Downstream agents depend heavily on extraction quality.
    """

    prompt = requirement_analysis_prompt.format(input=user_input)

    response = structured_llm.invoke(prompt)

    return response.model_dump()