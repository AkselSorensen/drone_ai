import cv2
import time
import os
from datetime import datetime

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

# Obtenir la date et l'heure actuelles pour les noms de fichiers
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

if not os.path.exists('videos'):
    os.makedirs('videos')
if not os.path.exists('photos'):
    os.makedirs('photos')

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# Inclure la date et l'heure dans le nom du fichier vidéo
out = cv2.VideoWriter(f'videos/video_{current_time}.mp4', fourcc, 20.0, (640, 480))

start_time = time.time()
photo_counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        # Dessiner un carré rouge autour du visage
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        # Dessiner un point rouge au centre du visage
        center_x = x + w // 2
        center_y = y + h // 2
        cv2.circle(frame, (center_x, center_y), radius=5, color=(0, 0, 255), thickness=-1)
    
    cv2.imshow('🎥 Face Detection 🎥', frame)
    
    out.write(frame)
    
    if time.time() - start_time >= 30:
        # Inclure la date et l'heure dans le nom du fichier photo
        photo_path = f'photos/photo_{photo_counter}_{current_time}.jpg'
        cv2.imwrite(photo_path, frame)
        print(f"📁 Photo saved to {photo_path}")
        photo_counter += 1
        start_time = time.time()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
