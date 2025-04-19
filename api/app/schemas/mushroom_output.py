from pydantic import BaseModel

class MushroomOutput(BaseModel):
    prediction: str