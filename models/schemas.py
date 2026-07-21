from pydantic import BaseModel, Field
from typing import List

class ContentGenerationRequest(BaseModel):
    url: str | None = None
    rss_feed: str | None = None
    raw_text: str | None = None

class GeneratedContentPackage(BaseModel):
    headline: str = Field(..., description="Strong, accurate headline")
    category: str = Field(..., description="One of the predefined categories")
    summary: str = Field(..., description="Detailed AI summary of the news")
    key_points: List[str] = Field(..., description="List of key takeaways")
    
    # Social Media Post variations
    social_post: str = Field(..., description="Primary social media post (professional/educational)")
    social_post_minimal: str = Field(..., description="Minimal version of the post")
    social_post_thread: List[str] = Field(..., description="Thread version of the post")
    hashtags: List[str] = Field(..., description="List of relevant hashtags")
    
    # Image Generation Package
    image_template: str = Field(..., description="Chosen visual template (e.g. 'Template 01 - Breaking News')")
    image_prompt: str = Field(..., description="Detailed image generation prompt")
    negative_prompt: str = Field(..., description="Negative prompt for image generation")
    colors: List[str] = Field(..., description="Suggested color palette")
    visual_style: str = Field(..., description="Design language description")
    aspect_ratio: str = Field(default="1:1", description="Aspect ratio of the image")
    image_size: str = Field(default="1080x1080", description="Export resolution")

class ApiResponse(BaseModel):
    status: str
    data: GeneratedContentPackage | None = None
    message: str | None = None
