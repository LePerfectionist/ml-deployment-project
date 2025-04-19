import os
from mushroom_model import train

def test_train_pipeline():
    # Clean up if needed
    if os.path.exists("model.pkl"):
        os.remove("model.pkl")

    train.train()
    assert os.path.exists("model.pkl")
