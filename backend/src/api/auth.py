from fastapi import APIRouter
from src.models.user_model import User
from src.services.user_service import register_user,login_user

router=APIRouter()
@router.post("/register")
def register(user:User):
    return register_user(user)

@router.post("/login/")
def login(user: User):
    return login_user(user)