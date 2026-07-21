import json
from typing import TypeVar, Type
from pydantic import BaseModel
from google import genai
from .base import BaseAIProvider

T = TypeVar('T', bound=BaseModel)

class GeminiProvider(BaseAIProvider):
    def __init__(self, api_key: str | None = None, model: str = "gemini-2.5-pro"):
        self.client = genai.Client(api_key=api_key)
        self.model = model

    async def generate_structured_response(self, prompt: str, schema: Type[T]) -> T:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config={
                'response_mime_type': 'application/json',
                'response_schema': schema,
            },
        )
        data = json.loads(response.text)
        return schema(**data)
