import json
from typing import TypeVar, Type
from pydantic import BaseModel
from openai import AsyncOpenAI
from .base import BaseAIProvider

T = TypeVar('T', bound=BaseModel)

class OllamaProvider(BaseAIProvider):
    def __init__(self, base_url: str = "http://localhost:11434/v1", model: str = "gemma:2b"):
        self.client = AsyncOpenAI(
            base_url=base_url,
            api_key="ollama" # Dummy key
        )
        self.model = model

    async def generate_structured_response(self, prompt: str, schema: Type[T]) -> T:
        # We try to use standard OpenAI structured output formatting.
        # Ollama supports this natively in recent versions.
        try:
            response = await self.client.beta.chat.completions.parse(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a professional content generator. Respond strictly in JSON matching the requested schema."},
                    {"role": "user", "content": prompt}
                ],
                response_format=schema,
                temperature=0.3
            )
            parsed_data = response.choices[0].message.parsed
            if parsed_data:
                return parsed_data
        except Exception as e:
            # Fallback for older Ollama versions or smaller models struggling with schema definitions.
            # We explicitly ask for JSON format.
            json_prompt = f"{prompt}\n\nIMPORTANT: You must return raw JSON only. The JSON must exactly conform to the following schema:\n{json.dumps(schema.model_json_schema())}"
            
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a professional content generator. Respond with raw JSON ONLY. No markdown formatting like ```json ... ```, just the plain JSON string."},
                    {"role": "user", "content": json_prompt}
                ],
                response_format={"type": "json_object"},
                temperature=0.3
            )
            
            content = response.choices[0].message.content
            # Clean up markdown formatting if the model output it anyway
            if content.startswith("```"):
                content = content.replace("```json", "").replace("```", "").strip()
            
            data = json.loads(content)
            return schema(**data)
