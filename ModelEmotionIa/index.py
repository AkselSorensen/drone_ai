
import cv2
import dlib
import numpy as np

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
facerec = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")
seuil_de_similarity = 0.6

def load_reference_image():
    reference_image = cv2.imread("image1.jpg")
    if reference_image is not None:
        dets = detector(reference_image, 1)
        if len(dets) > 0:
            shape = predictor(reference_image, dets[0])
            return np.array(facerec.compute_face_descriptor(reference_image, shape))
        else:
            print("Aucun visage trouvé dans l'image de référence.")
            return None
    else:
        print("Impossible de charger l'image de référence.")
        return None

reference_encoding = load_reference_image()

def face_recognition_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Impossible d'ouvrir la caméra.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        
        dets = detector(frame, 1)
        if len(dets) > 0:
            d = dets[0]
            shape = predictor(frame, d)
            face_encoding = np.array(facerec.compute_face_descriptor(frame, shape))
            similarity = np.linalg.norm(reference_encoding - face_encoding)
            if similarity < seuil_de_similarity:
                cv2.putText(frame, "Dangereux Criminel", (d.left(), d.top() - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            else:
                cv2.putText(frame, "inconnu(e)", (d.left(), d.top() - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            cv2.rectangle(frame, (d.left(), d.top()), (d.right(), d.bottom()), (0, 255, 0), 1)
        
        cv2.namedWindow('Face Recognition', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Face Recognition', 800, 600)
        cv2.imshow('Face Recognition', frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    face_recognition_camera()
