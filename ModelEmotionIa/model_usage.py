import requests
from tensorflow.keras.models import load_model
import cv2
import numpy as np

def download_and_preprocess_image(url):
    response = requests.get(url)
    image = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (48, 48))
    image = image.reshape(1, 48, 48, 1)
    return image

def predict_emotion(model, image_url):
    image = download_and_preprocess_image(image_url)
    prediction = model.predict(image)
    emotion = np.argmax(prediction)
    return emotion
