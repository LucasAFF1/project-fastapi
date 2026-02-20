from typing_extensions import Annotated

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from fastapi import Depends

from app.config import settings

class Base(DeclarativeBase):
    pass

postgresql_url = f"postgresql://postgres:{settings.DB_PASSWORD}@localhost:5432/my_database"

engine = create_engine(postgresql_url, echo=True)

Make_Session = sessionmaker(bind=engine) 

def get_session():
    with Make_Session() as session: 
        yield session 


SessionDep = Annotated[Session, Depends(get_session)]
