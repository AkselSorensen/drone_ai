import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def load_data(data_path):

    data = [] 
    labels = [] 

    for image_path in os.listdir(data_path):
        image = cv2.imread(os.path.join(data_path, image_path), cv2.IMREAD_GRAYSCALE)

        data.append(image)

        labels.append(label)
    return data, labels

def preprocess_data(data):

    pass

def split_data(data, labels):
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def main():
    data_path = "data/fer2013/train"
    data, labels = load_data(data_path)
    preprocessed_data = preprocess_data(data)
    X_train, X_test, y_train, y_test = split_data(preprocessed_data, labels)
    return X_train, X_test, y_train, y_test
