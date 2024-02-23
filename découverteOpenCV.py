import cv2

img = cv2.imread("image/rdm.jpeg", 0)
print(img.shape)

cv2.imshow("Image test", img)
k = cv2.waitKey(0)

if k == ord("s"):
    cv2.imwrite("image/rdm.jpg", img)
    print("L'image est sauvegardée.")
else:
    cv2.destroyAllWindows()
    print("Fenêtre détruite.")
