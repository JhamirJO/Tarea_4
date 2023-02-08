import cv2
import numpy as np

# cargar la imagen orignal
img1 = cv2.imread('prueba.png')
cv2.imshow("Original",img1)


#escala de grises
imgGris = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gris",imgGris)


#binarización
umbral = 85
mascara = np.uint8((imgGris<umbral)*255)
cv2.imshow("binaria",mascara)


cv2.waitKey(0)
cv2.destroyAllWindows()