from datetime import datetime, timedelta, timezone

from sqlalchemy import update
from sqlalchemy.orm import Session
import jwt

from app.schemas import Token
from app.auth.password import verify_password, hash_password
from app.exceptions import NotAuthenticated, UserNotFound
from app.config import settings
from app.auth.users_crud import get_user_by_username
from app.models import UserModel


def verify_user(username:str, password:str, session: Session)->bool:
    user = get_user_by_username(username=username, session=session)

    if not user:
        raise UserNotFound()

    verified  = verify_password(password, user.password)

    if not verified: 
        raise NotAuthenticated()
    
    return True 

def create_token(data:dict, expire_token_minutes: timedelta = timedelta(minutes=15))->str:
    to_encode = data.copy()
    exp = datetime.now(timezone.utc) + expire_token_minutes
    to_encode.update({"exp":exp})
    jwt_encoded = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    
    return jwt_encoded


def new_token(username:str, password:str, session: Session)->Token:
    verify_user(username, password, session)
    user = get_user_by_username(username, session)
    expire_token_minutes = timedelta(minutes=settings.EXPIRES_TOKEN_MINUTES)
    if user.is_staff: #type:ignore
        role = "staff"
    else:
        role = "basic" 
    access_token = create_token({"sub":username, "role":role, "exp":expire_token_minutes})
    
    return Token(access_token=access_token, token_type="bearer")



def new_staff(new_staff_username: str, session: Session): 
    user = get_user_by_username(new_staff_username, session)

    if user:
        user.is_staff = True
        
        session.commit()

        return {"msg": "Normal user turned into staff succesfully"}
    else: 
        raise UserNotFound()
    
