import openai # type: ignore
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

def generate_image(prompt: str):
    openai.api.key=OPENAI_API_KEY

    response =openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024*1024"
    )

    image_url=response["data"][0]["url"]
    return image_url