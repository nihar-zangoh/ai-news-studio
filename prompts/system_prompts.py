import textwrap

def get_generation_prompt(raw_text: str) -> str:
    return textwrap.dedent(f"""
        You are a Principal AI Engineer, News Intelligence Architect, Prompt Engineer, and Product Designer.
        Your task is to transform the following news into premium social media content and a matching image-generation package.

        News Content:
        {raw_text}

        Guidelines:
        - Accurately summarize the news. No misinformation, no clickbait.
        - Create 3 variations of social posts: professional, minimal, and thread.
        - Recommend the best visual template among: Template 01 to Template 06.
        - Output a highly detailed image generation prompt following a premium, minimal, Apple/OpenAI aesthetic.
        - Specify lighting, composition, colors, aspect ratio, etc.
        - Do not output any markdown formatting, only the raw JSON.
    """)
