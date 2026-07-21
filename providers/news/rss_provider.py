import feedparser
from .base import BaseNewsProvider

class RSSNewsProvider(BaseNewsProvider):
    async def fetch_news(self, source_url: str = "https://feeds.bbci.co.uk/news/world/rss.xml") -> str:
        """
        Fetches the latest news item from the given RSS feed.
        """
        feed = feedparser.parse(source_url)
        if not feed.entries:
            return "No news found in the RSS feed."
            
        # Get the top breaking news
        latest_entry = feed.entries[0]
        title = latest_entry.title
        summary = latest_entry.summary if 'summary' in latest_entry else ''
        
        raw_text = f"Title: {title}\nSummary: {summary}\nLink: {latest_entry.link}"
        return raw_text
