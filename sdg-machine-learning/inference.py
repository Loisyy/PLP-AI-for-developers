import tensorflow as tf
import numpy as np
from PIL import Image

def load_model(path="models/garment_model.h5"):
    return tf.keras.models.load_model(path)

def preprocess(image_path):
    img = Image.open(image_path).convert("RGB").resize((224,224))
    arr = np.array(img)/127.5 - 1.0
    return np.expand_dims(arr, 0)

def recommend(category, condition, user_text=None):
    # simple rules
    if condition == "good":
        if category in ["t-shirt","jeans","dress"]:
            return "Donate / Resell"
    if condition == "torn":
        return "Repair / Upcycle (patch, embroidery)"
    if condition == "worn":
        return "Recycle via textile recycling"
    return "Consider repair or creative upcycling"

if __name__ == "__main__":
    model = load_model()
    x = preprocess("assets/test_shirt.jpg")
    preds = model.predict(x)
    cat = preds['category'].argmax()
    cond = preds['condition'].argmax()
    print(recommend(cat, cond))
