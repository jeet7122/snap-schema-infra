"""
Centralized LLM configuration module used across all AI agents/services.

This module initializes and exposes a singleton Google Generative AI
LLM instance configured using LangChain integration.

The shared `llm` object is reused throughout the application to ensure:
- consistent model configuration
- reduced initialization overhead
- centralized temperature/model management
- standardized AI invocation behavior

Configuration:
- Provider: Google Generative AI
- Model: gemini-3.5-flash
- Temperature: 0.2

Used by:
- Requirement Analysis Agent
- Relationship Planner Agent
- Schema Generator Agent
- Architecture Review Agent

Environment:
- Requires valid Google Generative AI credentials in `.env`
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables before initializing LLM client
load_dotenv()


# Singleton LLM instance shared across the application
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0.2
)