from pydantic import BaseSettings

class Settings(BaseSettings):
    model_path: str = "model.pkl"
    log_level: str = "info"

settings = Settings()
