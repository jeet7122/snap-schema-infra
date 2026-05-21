from langchain_core.prompts import PromptTemplate


relationship_planner_prompt = PromptTemplate.from_template(
"""
You are a senior database architect.

Based on the extracted entities and features,
determine the relationships between entities.

RULES:

- Use normalized relational modeling
- Prefer:
  - many_to_one
  - one_to_many
  - many_to_many
- Generate realistic foreign key names
- Only generate meaningful relationships
- Do NOT generate relationships for:
  - statuses
  - enums
  - roles
  - categories
  - permissions
- Assume role-based systems should use:
  - shared users table
  - role field with CHECK constraints

INPUT:

Entities:
{entities}

Features:
{features}

OUTPUT FORMAT:

{{
  "relationships": [
    {{
      "source": "orders",
      "target": "users",
      "relationship_type": "many_to_one",
      "foreign_key": "customer_id"
    }}
  ]
}}
"""
)