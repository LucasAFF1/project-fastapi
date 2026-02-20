import uuid

from pydantic import BaseModel, EmailStr

class SignUpBase(BaseModel): 
    username: str 
    email: EmailStr 

    
class SignUpWrite(SignUpBase):
    password: str 
    

class SignUpRead(SignUpBase):
    id: uuid.UUID


class PasswordChange(BaseModel):
    old_password: str 
    new_password: str 



class Token(BaseModel):
    access_token: str
    token_type: str 
