import asyncio
import openai # type: ignore
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

async def generate_ai_response(prompt: str):
    openai.api.key=OPENAI_API_KEY

    response=await openai.ChatCompletion.acreate(
        model="gpt-4",
        message=[{"role": "user","content":prompt}],
        stearm=True
    )

    async for chunk in response:
        if "choices" in chunk and chunk["choices"]:
            yield chunk["choices"][0]["delta"].get("content","")