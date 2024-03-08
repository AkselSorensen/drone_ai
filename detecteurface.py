import cv2
import time
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

if not os.path.exists('videos'):
    os.makedirs('videos')
if not os.path.exists('photos'):
    os.makedirs('photos')

# Compter le nombre de fichiers vidéo existants dans le répertoire 'videos'
video_files = [f for f in os.listdir('videos') if f.endswith('.mp4')]
video_counter = len(video_files) + 1

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(f'videos/video{video_counter}.mp4', fourcc, 20.0, (640, 480))
start_time = time.time()
photo_counter = 0

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
    
    out.write(frame)
    
    if time.time() - start_time >= 20:
        photo_path = f'photos/photo_{photo_counter}.jpg'
        cv2.imwrite(photo_path, frame)
        print(f"Photo sauvegardez {photo_path}") # Ajout d'un message pour confirmer la sauvegarde
        photo_counter += 1
        start_time = time.time()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
