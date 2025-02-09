from fastapi import APIRouter
from src.tasks.image_task import generate_image_task

router=APIRouter()

@router.get("/generate/")
async def generate_image(prompt:str):
    task=generate_image_task(prompt)
    return {"task_id":task.id, "message":"Image generation started in the background"}