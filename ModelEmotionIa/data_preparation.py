import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def load_data(data_path):
    # Exemple de chargement de données
    # Cela dépend de la structure de vos données
    # Pour cet exemple, supposons que vous chargez des images et des étiquettes
    data = [] # Liste pour stocker les images
    labels = [] # Liste pour stocker les étiquettes
    # Charger les données et les étiquettes ici
    # Par exemple, si vous chargez des images depuis un répertoire :
    for image_path in os.listdir(data_path):
        image = cv2.imread(os.path.join(data_path, image_path), cv2.IMREAD_GRAYSCALE)
        # Prétraitez l'image ici si nécessaire
        data.append(image)
        # Ajoutez l'étiquette correspondante à labels
        # Par exemple, si vous avez une étiquette pour chaque image :
        labels.append(label)
    return data, labels

def preprocess_data(data):
    # Normaliser les images
    # Convertir les étiquettes en one-hot encoding
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
