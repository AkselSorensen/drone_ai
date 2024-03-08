# 🎥 Projet de Détection de Visages et Capture Vidéo/Photos 📸

Ce projet utilise OpenCV pour détecter les visages dans une vidéo en temps réel, enregistrer la vidéo et prendre des photos à intervalles réguliers.

## 🚀 Démarrage rapide

1. **Installer les dépendances** : Assurez-vous d'avoir Python et OpenCV installés sur votre système.

2. **Cloner le projet** : Clonez ce dépôt ou téléchargez le code source.

3. **Exécuter le script** : Exécutez le script Python principal pour commencer la détection de visages et l'enregistrement de la vidéo.

## 📁 Structure du projet

- `detecteurface.py` : Le script principal qui gère la détection de visages, l'enregistrement de la vidéo et la prise de photos.
- `videos/` : Le répertoire où les vidéos enregistrées sont stockées.
- `photos/` : Le répertoire où les photos prises à intervalles réguliers sont stockées.

## 📝 Comment ça marche

1. **Détection de visages** : Utilise le classificateur de visage Haar cascade pour détecter les visages dans la vidéo en temps réel.

2. **Enregistrement de la vidéo** : Enregistre la vidéo en format MP4 dans le répertoire `videos/`.

3. **Prise de photos** : Pren des photos à intervalles réguliers (par exemple, toutes les 30 secondes) et les stocke dans le répertoire `photos/`.

## 🛠️ Configuration

- **Changement de l'intervalle de prise de photos** : Modifiez la valeur dans la condition `if time.time() - start_time >= 30:` pour changer l'intervalle de prise de photos.

- **Changement du format de la vidéo** : Modifiez le codec dans `fourcc = cv2.VideoWriter_fourcc(*'mp4v')` pour changer le format de la vidéo enregistrée.

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus d'informations.

## 🙏 Remerciements

Merci d'utiliser ce projet. N'hésitez pas à contribuer ou à partager vos améliorations !

