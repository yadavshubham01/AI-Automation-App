from passlib.context import CryptContext
from src.utils.jwt_handler import create_jwt_token
from src.models.user_model import User

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

fake_user_db= {}

def register_user(user:User):
    if user.username in fake_user_db:
        return {"error": "User already exists"}
    

    hashed_password = pwd_context.hash(user.password)
    fake_user_db[user.username]=hashed_password
    return {"message" : "USER register successfully"}

def login_user(user:User):
    if user.username not in fake_user_db:
        return {"error" : "Invalid username or password"}
    
    stored_pass=fake_user_db[user.username]
    if not pwd_context.verify(user.password,stored_pass):
        return {"error": "Invalid username or password"}
    
    
    token=create_jwt_token({"sub":user.username})
    return {"acess_token":token}