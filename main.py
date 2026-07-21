from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from api.routes import generate
from core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="Transforms news into premium social media content and image generation packages.",
    version="1.0.0"
)

app.include_router(generate.router, prefix="/api/v1")

@app.get("/")
async def serve_frontend():
    return FileResponse("frontend/index.html")

app.mount("/", StaticFiles(directory="frontend"), name="frontend")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

