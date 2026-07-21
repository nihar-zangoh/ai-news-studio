from fastapi import APIRouter, HTTPException, Depends
from models.schemas import ContentGenerationRequest, ApiResponse, GeneratedContentPackage
from services.content_generator import ContentGeneratorService
from providers.ai.mock_provider import MockAIProvider
from providers.ai.gemini_provider import GeminiProvider
from providers.news.rss_provider import RSSNewsProvider
from core.config import settings

router = APIRouter()

def get_content_generator() -> ContentGeneratorService:
    if settings.GEMINI_API_KEY:
        ai_provider = GeminiProvider(api_key=settings.GEMINI_API_KEY)
    else:
        ai_provider = MockAIProvider()
    return ContentGeneratorService(ai_provider=ai_provider)

@router.post("/generate", response_model=ApiResponse)
async def generate_content(
    request: ContentGenerationRequest,
    generator: ContentGeneratorService = Depends(get_content_generator)
):
    try:
        if not request.raw_text and not request.url:
            raise HTTPException(status_code=400, detail="Must provide raw_text or url")
            
        raw_text = request.raw_text or f"Fetching content from {request.url} is not yet implemented. Please provide raw text."
        
        content_package = await generator.generate_content(raw_text)
        
        return ApiResponse(
            status="success",
            data=content_package,
            message="Content generated successfully"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate-breaking-news", response_model=ApiResponse)
async def generate_breaking_news(
    generator: ContentGeneratorService = Depends(get_content_generator)
):
    try:
        news_fetcher = RSSNewsProvider()
        raw_text = await news_fetcher.fetch_news("http://feeds.bbci.co.uk/news/world/rss.xml")
        
        content_package = await generator.generate_content(raw_text)
        
        return ApiResponse(
            status="success",
            data=content_package,
            message="Breaking news content generated successfully"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

