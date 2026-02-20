from pydantic_settings import BaseSettings, SettingsConfigDict
from datetime import datetime, timezone


class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env")

    EXPIRES_TOKEN_MINUTES: int
    SECRET_KEY: str 
    ALGORITHM : str = "HS256"
    DB_PASSWORD: str 

    

settings = Settings() #type: ignore

def get_datetime_utc():
    return datetime.now(timezone.utc)







