import cv2

img = cv2.imread("image/rdm.jpeg", 0)
print(img.shape)

cv2.imshow("Images test",img)
cv2.waitKey(0)
cv2.destroyAllwindows()

cv2.imwrite("image/rdm.jpg",img)