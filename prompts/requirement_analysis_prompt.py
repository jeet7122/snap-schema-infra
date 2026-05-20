from langchain_core.prompts import PromptTemplate

requirement_analysis_prompt = PromptTemplate.from_template(
"""
You are a senior software architect.

Analyze the user requirements and extract:

1. Main entities
2. Core platform features

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