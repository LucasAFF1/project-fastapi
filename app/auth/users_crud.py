from sqlalchemy import update, select
from sqlalchemy.orm import Session
from pydantic import EmailStr

from app.models import UserModel 
from app.schemas import SignUpWrite, PasswordChange
from app.exceptions import UserAlreadyExist, IncorrectPassword
from app.auth.password import hash_password, verify_password


def sign_up(user: SignUpWrite, session: Session)->UserModel:
    username_already_exists = session.execute(select(UserModel).where(UserModel.username == user.username)).scalars().first()
    email_already_exists= session.execute(select(UserModel).where(UserModel.email == user.email)).scalars().first()
    
    if email_already_exists or username_already_exists: 
        raise UserAlreadyExist()
    
    user.password = hash_password(user.password)
    
    user_db = UserModel(username=user.username, email=user.email, password=user.password)

    session.add(user_db)
    session.commit()
    session.refresh(user_db)

    return user_db 


def get_user_by_username(username:str, session)->UserModel:
    user = session.execute(select(UserModel).where(UserModel.username == username)).scalars().first()

    return user

def get_user_by_id(id: int, session)->UserModel:
    user = session.get(UserModel, id)

    return user 

def get_user_by_email(email: EmailStr, session)->UserModel:
    user = session.execute(select(UserModel).where(UserModel.email == email)).scalars().first()

    return user 

def delete_user(id: int, session)->dict[str, str]:
    user = get_user_by_id(id, session)

    session.delete(user)
    session.commit()

    return {"msg": "user deleted"}

def update_password(session: Session, user: UserModel, password:str): 
    update(UserModel).where(UserModel.id == user.id).values(password=password)
    
    session.commit()

def change_password(session: Session, current_user: UserModel, creds: PasswordChange):
    if not verify_password(current_user.password, hash_password(creds.old_password)):
        raise IncorrectPassword()
    update_password(session, current_user, creds.new_password)

    
