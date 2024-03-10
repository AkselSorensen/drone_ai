import os
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


