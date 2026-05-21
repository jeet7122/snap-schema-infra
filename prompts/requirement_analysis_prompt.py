from langchain_core.prompts import PromptTemplate


requirement_analysis_prompt = PromptTemplate.from_template(
"""
You are a senior software architect.

Analyze the user requirements and extract:

1. Real database entities
2. Core platform features

IMPORTANT RULES:

- Extract ONLY true relational entities.
- Do NOT create entities for:
  - roles
  - statuses
  - permissions
  - categories
  - enums
  - types
- Prefer modeling those as:
  - ENUM values
  - CHECK constraints
  - role fields
- Example:
  - "admins", "drivers", "customers"
    should become:
    users + role field
- Example:
  - order statuses should NOT become tables

Return ONLY valid JSON.

USER INPUT:
{input}

OUTPUT FORMAT:

{{
  "entities": [
    "users"
  ],
  "features": [
    "authentication"
  ]
}}
"""
)