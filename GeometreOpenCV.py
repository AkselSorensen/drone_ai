import cv2
import matplotlib.pyplot as plt


img = cv2.imread("image/rdm.jpg")

#dimensions de l'image
height, width, _ = img.shape

#coordonnées du rectangle
x1, y1 = width // 4, height // 4  # coin supérieur gauche
x2, y2 = width * 3 // 4, height * 3 // 4  # coin inférieur droit

# rectangle rouge 
cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 5)

#  point rouge au centre du rectangle
center_x = (x1 + x2) // 2
center_y = (y1 + y2) // 2
cv2.circle(img, (center_x, center_y), 5, (0, 0, 255), 5)

# Convertir l'image en format compatible avec Matplotlib (BGR -> RGB)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


plt.imshow(img_rgb)
plt.axis('off')  
plt.show()
