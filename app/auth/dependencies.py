from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
import jwt 

from app.config import settings
from app.exceptions import InvalidToken, NotAuthorized, NotActiveUser
from app.database import SessionDep
from app.models import UserModel
from app.auth.users_crud import get_user_by_username

oauth2_schema = OAuth2PasswordBearer("token")


def current_user(session: SessionDep, token: Annotated[str, Depends(oauth2_schema)])->UserModel: 
    try: 
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username = payload["sub"]
        if not username: 
            raise InvalidToken()
    except: 
        raise InvalidToken()
    
    user = get_user_by_username(username, session)

    if not user:
        raise InvalidToken()
    if not user.is_active:
        raise NotActiveUser()
    
    return user 


def require_staff(user: Annotated[UserModel, Depends(current_user)])->UserModel:
    if not user.is_staff:
        raise NotAuthorized()
    return user 


CurrentUser = Annotated[UserModel, Depends(current_user)]
RequireStaff = Annotated[UserModel, Depends(require_staff)]