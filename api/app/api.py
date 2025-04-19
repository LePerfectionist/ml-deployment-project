from fastapi import APIRouter
from api.app.schemas.mushroom_input import MushroomInput
from api.app.schemas.mushroom_output import MushroomOutput
from mushroom_model.predict import load_model, predict_one

from api.app.config import settings
model, encoders = load_model(settings.model_path)


router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/predict", response_model=MushroomOutput)
def predict(input: MushroomInput):
    pred = predict_one(input.model_dump(by_alias=True), model, encoders)
    return {"prediction": "Edible" if pred == "e" else "Poisonous"}