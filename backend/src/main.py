from fastapi import FastAPI
from src.api import gpt ,image,ws,auth

app=FastAPI(title='AI Automation TOOL')

app.include_router(gpt.router,prefix='/gpt',tags=["GPT"])
app.include_router(auth.router,prefix='/auth',tags=["Auth"])
app.include_router(image.router,prefix='/image',tags=["IMAGE"])
app.include_router(ws.router,prefix='/ws',tags=["WebSockets"])

@app.get("/")
def read_root():
    return {"msg ":"AI Automation Backend is running 🚀"}
