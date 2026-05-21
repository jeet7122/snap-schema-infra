"""
Relationship planning agent responsible for generating entity relationships
based on extracted entities and application features.

This agent uses structured LLM output generation to produce normalized
database relationship mappings between entities such as:
- one-to-one
- one-to-many
- many-to-many

The generated relationship plan is later consumed by:
- Schema Generation Agent
- SQL Compiler
- Metadata Builder

Flow:
1. Accept extracted entities and features
2. Inject data into relationship planner prompt
3. Invoke structured LLM response generation
4. Return validated relationship model output

Used in:
- schema_service
"""

from core.llm import llm
from prompts.relationship_planner_prompt import relationship_planner_prompt
from models.schema_models import RelationShipPlan


# Configure structured response parsing using Pydantic schema
structured_llm = llm.with_structured_output(RelationShipPlan)


def generate_relationships(entities: list[str], features: list[str]):
    """
    Generate database relationship mappings between extracted entities.

    This method analyzes the provided entities and application features
    to infer logical database relationships required for schema generation.

    The response is validated against the `RelationShipPlan` schema
    before being returned.

    Args:
        entities:
            List of extracted domain entities identified during
            requirement analysis.

        features:
            List of application features/modules used to infer
            entity interaction patterns.

    Returns:
        dict:
            Structured relationship mapping containing inferred
            entity associations and relationship metadata.

    Used by:
        - schema_service.generate_schema_service()

    Notes:
        - Uses structured LLM output validation.
        - Prompt formatting converts entity/feature lists into
          comma-separated context strings.
        - Relationship inference is AI-driven and context-aware.
    """

    prompt = relationship_planner_prompt.format(
        entities=", ".join(entities),
        features=", ".join(features)
    )

    response = structured_llm.invoke(prompt)

    return response.model_dump()