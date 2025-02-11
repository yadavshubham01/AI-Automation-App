from fastapi import FastAPI
from src.api import gpt ,image,ws,auth
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI(title='AI Automation TOOL')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific origins for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(gpt.router,prefix='/gpt',tags=["GPT"])
app.include_router(auth.router,prefix='/auth',tags=["Auth"])
app.include_router(image.router,prefix='/image',tags=["IMAGE"])
app.include_router(ws.router,prefix='/ws',tags=["WebSockets"])

@app.get("/")
def read_root():
    return {"msg ":"AI Automation Backend is running 🚀"}
