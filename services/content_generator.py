from models.schemas import GeneratedContentPackage
from providers.ai.base import BaseAIProvider

class ContentGeneratorService:
    def __init__(self, ai_provider: BaseAIProvider):
        self.ai_provider = ai_provider

    async def generate_content(self, raw_news_text: str) -> GeneratedContentPackage:
        prompt = f"""
        You are an expert AI News Content Studio engine. 
        Your task is to analyze the following news article and generate a premium social media content package and an image generation prompt.
        
        Article Content:
        {raw_news_text}
        
        Generate the content according to the required schema, ensuring high quality, no hallucinations, and a premium visual description.
        """
        
        # Call the AI provider
        return await self.ai_provider.generate_structured_response(
            prompt=prompt,
            schema=GeneratedContentPackage
        )
