import cv2

def main():
    # Initialisation de la capture vidéo
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erreur lors de l'ouverture de la caméra.")
        return

    while True:
        # Capture des images de la caméra
        ret, frame = cap.read()
        if not ret:
            print("Erreur lors de la capture de l'image.")
            break

        # Affichage de l'image
        cv2.imshow("Caméra", frame)

        # 'q' pour quitter la boucle
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libération des ressources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
