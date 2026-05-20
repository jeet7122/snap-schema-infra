from core.llm import llm
from prompts.relationship_planner_prompt import relationship_planner_prompt
from models.schema_models import RelationShipPlan

structured_llm = llm.with_structured_output(RelationShipPlan)


def generate_relationships(entities: list[str], features: list[str]):
    prompt = relationship_planner_prompt.format(
        entities=", ".join(entities),
        features=", ".join(features)
    )
    response = structured_llm.invoke(prompt)
    return response.model_dump()