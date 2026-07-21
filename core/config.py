from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    # App Settings
    APP_NAME: str = "AI News Content Studio"
    DEBUG: bool = True
    
    # API Keys
    OPENAI_API_KEY: str | None = None
    GEMINI_API_KEY: str | None = None
    ANTHROPIC_API_KEY: str | None = None
    GROQ_API_KEY: str | None = None

    # Allowed categories for news
    CATEGORIES: List[str] = [
        "Artificial Intelligence", "Technology", "Startups", "Programming", 
        "Open Source", "Cybersecurity", "Cloud", "Robotics", "Gaming", 
        "Mobile", "Research", "Business"
    ]
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
