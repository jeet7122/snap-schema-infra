"""
Architecture review agent responsible for validating and reviewing
generated database schema architecture.

This agent evaluates the generated schema for:
- structural consistency
- scalability considerations
- normalization quality
- relationship correctness
- architectural improvements

The review output helps identify potential schema design issues
before SQL compilation or deployment.

Flow:
1. Accept generated schema
2. Inject schema into architecture review prompt
3. Invoke structured AI review process
4. Return architectural feedback and recommendations
"""

from core.llm import llm
from prompts.architect_review_prompt import architecture_review_prompt
from models.schema_models import ArchitectureReview


# Configure structured architecture review output
structured_llm = llm.with_structured_output(ArchitectureReview)


def review_architecture(schema: dict):
    """
    Perform AI-driven architectural review of generated schema design.

    This method evaluates schema quality and provides feedback
    regarding database design decisions and potential improvements.

    Args:
        schema:
            Generated database schema structure to review.

    Returns:
        dict:
            Structured architectural review containing validation
            feedback, recommendations, and improvement suggestions.

    Used by:
        - schema_service.generate_schema_service()

    Notes:
        - Helps improve schema quality before SQL generation.
        - Review logic is context-aware and AI-driven.
        - Output is validated using ArchitectureReview schema.
    """

    prompt = architecture_review_prompt.format(schema=schema)

    response = structured_llm.invoke(prompt)

    return response.model_dump()