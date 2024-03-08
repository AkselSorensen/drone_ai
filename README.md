Drone Tello avec Reconnaissance Faciale
Ce projet permet de détecter et suivre des visages en temps réel à l’aide d’un drone Tello. Nous utilisons la bibliothèque OpenCV pour la détection des visages et le contrôle du drone.

Prérequis
Python 3.6 ou supérieur
Tello SDK (assurez-vous que votre drone est connecté au réseau Wi-Fi)
Bibliothèques Python : opencv-python, numpy, djitellopy
Installation
Clonez ce dépôt sur votre machine locale :
git clone https://github.com/votre-utilisateur/Drone-Tello-Face-Recognition.git

Installez les dépendances Python :
pip install -r requirements.txt

Utilisation
Connectez-vous au réseau Wi-Fi du drone Tello.
Exécutez le script principal :
python main.py
Le drone décollera automatiquement et commencera à diffuser la vidéo vers votre ordinateur.
La détection des visages sera affichée sur la vidéo en temps réel.
Fonctionnalités
Détection des visages : Le drone détecte les visages dans le flux vidéo.
Suivi des visages : Le drone suit automatiquement le visage le plus proche.
Centrage automatique : Le drone ajuste sa position pour maintenir le visage au centre de l’image.
Prochaines étapes
Voici quelques améliorations possibles pour ce projet :

Gérer la détection de plusieurs utilisateurs.
Optimiser le code pour des performances vidéo améliorées.
Implémenter un modèle d’apprentissage pour la reconnaissance faciale.
