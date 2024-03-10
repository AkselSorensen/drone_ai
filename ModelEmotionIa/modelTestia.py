import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def load_data(data_path):
    # Exemple de chargement de données
    # Cela dépend de la structure de vos données
    data = [] # Liste pour stocker les images
    labels = [] # Liste pour stocker les étiquettes
    # Charger les données et les étiquettes ici
    for image_path in os.listdir(data_path):
        image = cv2.imread(os.path.join(data_path, image_path), cv2.IMREAD_GRAYSCALE)
        # Prétraitez l'image ici si nécessaire
        data.append(image)
        # Ajoutez l'étiquette correspondante à labels
        # Par exemple, si vous avez une étiquette pour chaque image :
        labels.append(label)
    return data, labels

# Les autres fonctions restent inchangées...
