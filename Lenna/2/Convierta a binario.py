import cv2

img = cv2.imread('prueba.png', cv2.IMREAD_COLOR)
cv2.imshow("original", img)

# binarización

img2 = cv2.imread('prueba.png', 2)
ret, bw_img = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Binaria", bw_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

