import requests
import os 
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GPT_ENDPOINT = "https://api.openai.com/v1/chat/completions"

async def generate_gpt_response(prompt:str):
    headers={
        "Authorization":f"Bearer {OPENAI_API_KEY}",
        "Content-Type":"application/json"
    }
    data ={
        "model":"gpt-4",
        "message":[{"role":"user","content":prompt}]
    }

    reponse=requests.post(GPT_ENDPOINT,json=data,headers=headers)

    if reponse.status_code== 200:
        return reponse.json()["choices"][0]