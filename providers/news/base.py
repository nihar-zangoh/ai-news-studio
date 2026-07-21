from abc import ABC, abstractmethod

class BaseNewsProvider(ABC):
    @abstractmethod
    async def fetch_news(self, source_url: str) -> str:
        """
        Fetches raw content from a news source.
        """
        pass
