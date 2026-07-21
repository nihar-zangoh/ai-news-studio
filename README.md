# AI News Content Studio

Transforms the latest news into premium social media content and matching image-generation packages.

## Setup

1. Create a virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Configure environment variables in `.env`:
```
GEMINI_API_KEY=your_key
OPENAI_API_KEY=your_key
```

3. Run the development server:
```bash
fastapi dev main.py
```

## Architecture
- `api/`: FastAPI endpoints.
- `models/`: Pydantic input/output schemas.
- `services/`: Business logic orchestration.
- `providers/`: Abstractions for AI (Gemini, OpenAI, Mock) and News Fetching.
- `prompts/` & `templates/`: AI prompts and visual layouts.
