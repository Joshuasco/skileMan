from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    # This allows Pydantic to automatically look for an environment variable 
    SECRET_KEY : str = Field(
        validation_alias="SECRET_KEY"
    )

    # named DATABASE_URL. If not found, it uses the default SQLite string.
    DATABASE_URL: str = Field(
        default="sqlite:///./skile_man.db", 
        validation_alias="DATABASE_URL"
    )

    # Automatically casts the string from os.getenv to an integer
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(
        default=30, 
        validation_alias="ACCESS_TOKEN_EXPIRE_MINUTES"
    )
    # PyJWT algorithm type
    ALGORITHM: str = "HS256"  
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()




