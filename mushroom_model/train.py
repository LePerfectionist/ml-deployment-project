from pipeline import load_data, encode_features
from sklearn.ensemble import RandomForestClassifier
import pickle

MODEL_PATH = "api/app/artifacts/model.pkl"

def train():
    df = load_data("dataset/mushrooms.csv")
    X, y, encoders = encode_features(df)
    model = RandomForestClassifier()
    model.fit(X, y)
    with open(MODEL_PATH, "wb") as f:
        pickle.dump((model, encoders), f)

if __name__ == "__main__":
    train()