import pickle

def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

def predict_one(input_dict):
    model, encoders = load_model()
    encoded = [encoders[col].transform([input_dict[col]])[0] for col in input_dict]
    pred = model.predict([encoded])[0]
    return encoders["class"].inverse_transform([pred])[0]