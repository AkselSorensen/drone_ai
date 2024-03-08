import cv2
import time
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

start_time = time.time()
photo_counter = 0

if not os.path.exists('photos'):
    os.makedirs('photos')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        
        center_x = x + w // 2
        center_y = y + h // 2
        
        cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)

    cv2.imshow('Face Detection', frame)
    

    if time.time() - start_time >= 30:
        cv2.imwrite('photos/photo_{photo_counter}.jpg', frame)
        photo_counter += 1
        start_time = time.time() 

    # Quitter la boucle si la touche 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la capture vidéo et fermer les fenêtres
cap.release()
cv2.destroyAllWindows()
