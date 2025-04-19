from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_path: str = "api/app/artifacts/model.pkl"

settings = Settings()
