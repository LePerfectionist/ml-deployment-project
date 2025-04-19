from mushroom_model.pipeline import load_data, encode_features
from sklearn.ensemble import RandomForestClassifier
import pickle

def train():
    df = load_data("dataset/mushrooms.csv")
    X, y, encoders = encode_features(df)
    model = RandomForestClassifier()
    model.fit(X, y)
    with open("model.pkl", "wb") as f:
        pickle.dump((model, encoders), f)

if __name__ == "__main__":
    train()