import json
from typing import TypeVar, Type
from pydantic import BaseModel
from .base import BaseAIProvider

T = TypeVar('T', bound=BaseModel)

class MockAIProvider(BaseAIProvider):
    async def generate_structured_response(self, prompt: str, schema: Type[T]) -> T:
        # Returns a dummy response based on schema (for testing)
        dummy_data = {
            "headline": "Sample Breaking News Headline",
            "category": "Technology",
            "summary": "This is a comprehensive summary of the news article provided.",
            "key_points": ["Point 1", "Point 2", "Point 3"],
            "social_post": "Check out this amazing news! 🚀",
            "social_post_minimal": "Amazing news just dropped.",
            "social_post_thread": ["1/ Check out this news", "2/ It's amazing"],
            "hashtags": ["#tech", "#news", "#innovation"],
            "image_template": "Template 01 - Breaking News",
            "image_prompt": "A modern, minimalist illustration of technology breaking news.",
            "negative_prompt": "clutter, text, watermark",
            "colors": ["#1A1A1A", "#F5F5F5", "#007AFF"],
            "visual_style": "Premium, minimal, glassmorphism",
            "aspect_ratio": "1:1",
            "image_size": "1080x1080"
        }
        return schema(**dummy_data)
