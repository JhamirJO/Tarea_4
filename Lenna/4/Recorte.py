import cv2

image = cv2.imread('prueba.png')

#Recortar una imagen
imageOut = image[5:140, 135:277]
cv2.imshow('Imagen de entrada', image)
cv2.imshow('Imagen de salida', imageOut)
cv2.waitKey(0)
cv2.destroyAllWindows()