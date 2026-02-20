from typing import Annotated 

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from app.auth.service import new_token, new_staff
from app.schemas import Token
from app.auth.dependencies import current_user, require_staff
from app.models import UserModel
from app.schemas import SignUpRead, SignUpWrite
from app.database import SessionDep
from app.auth.users_crud import sign_up


auth_router = APIRouter()


@auth_router.post("/signup", 
                  response_model=SignUpRead,
                  status_code=status.HTTP_201_CREATED
                )

def register(user: SignUpWrite, session: SessionDep):
    new_user = sign_up(user, session)
    return new_user 


@auth_router.post("/login",
                  response_model=Token,
                  status_code=status.HTTP_200_OK)
def create_token(form: Annotated[OAuth2PasswordRequestForm, Depends()], session : SessionDep):
    token = new_token(form.username, form.password, session)
    return token 


@auth_router.get("/users/me",
                 response_model=SignUpRead, 
                 status_code=status.HTTP_202_ACCEPTED)
def get_current_user(user =  Depends(current_user)):
    return user 


@auth_router.patch("/users/staff/{username}", status_code=status.HTTP_202_ACCEPTED)
def make_staff(username:str, 
                     current_user: Annotated[UserModel, Depends(require_staff)],
                     session: SessionDep):
    new_staff(username, session)
    return {"msg": "normal user converted into staff succesfully"}
