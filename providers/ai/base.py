from abc import ABC, abstractmethod
from typing import TypeVar, Type
from pydantic import BaseModel

T = TypeVar('T', bound=BaseModel)

class BaseAIProvider(ABC):
    @abstractmethod
    async def generate_structured_response(self, prompt: str, schema: Type[T]) -> T:
        """
        Generates a structured response based on the prompt and Pydantic schema.
        """
        pass
