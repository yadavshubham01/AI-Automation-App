from fastapi import APIRouter,Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from src.utils.jwt_handler import verfiy_jwt_token
from src.celery_app import celery
from src.tasks.gpt_task import process_gpt_task

router =APIRouter()

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token:str=Depends(oauth2_scheme)):
    user=verfiy_jwt_token(token)
    if not user :
        raise HTTPException(status_code=401,detail="Invalid token")
    return user

@router.get("/generate")
async def generate_response(prompt:str,user: dict=Depends(get_current_user)):
    task=process_gpt_task.delay(prompt)
    return {"task_id": task.id,"message":"Processing in background"}

@router.get("/task_status")
async def task_status(task_id:str):
    task=celery.AsyncResult(task_id)
    return {"status":task.status, "result" : task.result}