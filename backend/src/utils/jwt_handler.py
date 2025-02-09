import jwt
import os
from datetime import datetime,timedelta
from dotenv import load_dotenv

load_dotenv
SECRET_KEY =os.getenv("SECRET_KEY","shubham@123")
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES =60


def create_jwt_token(data:dict):
    expire=datetime.utcnow() +timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data.update({"exp": expire})
    return jwt.encode(data,SECRET_KEY,algorithm=ALGORITHM)

def verfiy_jwt_token(token:str):
    try:
        decoded_data=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return decoded_data
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None