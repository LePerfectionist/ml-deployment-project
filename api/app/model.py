# app/model.py
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_and_save_model():
    iris = load_iris()
    X, y = iris.data, iris.target
    clf = RandomForestClassifier()
    clf.fit(X, y)
    with open("app/model.pkl", "wb") as f:
        pickle.dump(clf, f)

if __name__ == "__main__":
    train_and_save_model()
