import pickle

MODEL_PATH = "api/app/artifacts/model.pkl"
def load_model(model_path):
    with open(model_path, "rb") as f:
        return pickle.load(f)

def predict_one(input_dict, model, encoders):
    encoded = [encoders[col].transform([input_dict[col]])[0] for col in input_dict]
    pred = model.predict([encoded])[0]
    return encoders["class"].inverse_transform([pred])[0]