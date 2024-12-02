import pickle
import numpy as np

def load_model():
    """Завантажує збережену модель машинного навчання."""
    with open("model/model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

def make_prediction(model, data):
    """Робить передбачення на основі ринкових даних."""
    # Підготовка даних (наприклад, останні 5 цін)
    features = data['close'].tail(5).astype(float).values
    features = np.expand_dims(features, axis=0)
    
    prediction = model.predict(features)
    return prediction[0]
