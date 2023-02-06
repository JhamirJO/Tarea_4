import cv2


# cargar la imagen
img1 = cv2.imread('prueba.png')
img2 = cv2.imread('prueba.png', 2)

cv2.imshow("Original",img1)
ret, bw_img = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)

# converting to its binary form
bw = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary", bw_img)

cv2.waitKey(0)
cv2.destroyAllWindows()