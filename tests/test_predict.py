from mushroom_model.predict import predict_one

def test_prediction_edible():
    sample = {
        "cap-shape": "x", "cap-surface": "s", "cap-color": "n", "bruises": "t",
        "odor": "a", "gill-attachment": "f", "gill-spacing": "c", "gill-size": "n",
        "gill-color": "k", "stalk-shape": "e", "stalk-root": "e",
        "stalk-surface-above-ring": "s", "stalk-surface-below-ring": "s",
        "stalk-color-above-ring": "w", "stalk-color-below-ring": "w",
        "veil-type": "p", "veil-color": "w", "ring-number": "o", "ring-type": "p",
        "spore-print-color": "k", "population": "s", "habitat": "u"
    }
    pred = predict_one(sample)
    assert pred in ["e", "p"]
