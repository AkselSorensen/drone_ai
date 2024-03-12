import cv2
import dlib
import numpy as np

# Charger le modèle pré-entraîné de dlib pour la reconnaissance faciale
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Fonction pour détecter et dessiner les points de repère du visage
def detect_and_draw_landmarks(image):
    dets = detector(image, 1)
    for k, d in enumerate(dets):
        shape = predictor(image, d)
        for i in range(1, 68):
            cv2.circle(image, (shape.part(i).x, shape.part(i).y), 2, (0, 255, 0), -1)
    return image

# Fonction pour capturer la vidéo de la caméra et appliquer la reconnaissance faciale
def face_recognition_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5) # Réduire la taille de l'image pour accélérer le traitement
        frame = detect_and_draw_landmarks(frame)
        cv2.imshow('Face Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    face_recognition_camera()
