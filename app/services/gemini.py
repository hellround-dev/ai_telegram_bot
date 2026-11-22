from google import genai
from app.config import settings

client = genai.Client(api_key=settings.gemini_api_key)


async def generate_text(promt: str) -> str:
    response = await client.aio.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=promt,
    )
    return response.text
