from pydantic import BaseModel

class Settings(BaseModel):
    log_level: str = "info"

settings = Settings()
