#!/usr/bin/env python3
"""
Model configuration for the Competitor Analysis Agent
Structured schemas for inter-agent data validation
"""

from agno.models.openrouter import OpenRouter
from agno.models.openai.like import OpenAILike
from pydantic import BaseModel
from typing import Optional, List
from .config import (
    COORDINATOR_MODEL, AGENT_MODEL,
    LLM_PROVIDER, BHARATCODE_API_KEY, BHARATCODE_MODEL, BHARATCODE_BASE_URL
)


class CompetitorProfile(BaseModel):
    """Structured competitor profile for data validation"""
    name: str
    address: Optional[str] = None
    rating: Optional[float] = None
    review_count: Optional[int] = None
    price_tier: Optional[str] = None  # "Budget" | "Mid-range" | "Premium"
    website: Optional[str] = None
    hours: Optional[str] = None


class DiscoveryOutput(BaseModel):
    """Structured discovery output for inter-agent communication"""
    competitors: List[CompetitorProfile]
    target_company: str
    location: str


def coordinator_model(max_tokens: int = 4096):
    """Get the coordinator model instance"""
    if LLM_PROVIDER == "bharatcode":
        return OpenAILike(
            id=BHARATCODE_MODEL,
            api_key=BHARATCODE_API_KEY,
            base_url=BHARATCODE_BASE_URL,
            max_tokens=max_tokens
        )
    return OpenRouter(id=COORDINATOR_MODEL, max_tokens=max_tokens)


def agent_model(max_tokens: int = 4096):
    """Get the agent model instance"""
    if LLM_PROVIDER == "bharatcode":
        return OpenAILike(
            id=BHARATCODE_MODEL,
            api_key=BHARATCODE_API_KEY,
            base_url=BHARATCODE_BASE_URL,
            max_tokens=max_tokens
        )
    return OpenRouter(id=AGENT_MODEL, max_tokens=max_tokens)
