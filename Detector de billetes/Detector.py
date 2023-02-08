import cv2
import numpy as np

def detect_bill(img):
    # Convertir imagen a HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Definir los rangos de color para cada billete
    lower_green = np.array([25, 50, 50])
    upper_green = np.array([80, 255, 255])
    lower_yellow = np.array([10, 80, 80])
    upper_yellow = np.array([20, 255, 255])
    lower_fuchsia = np.array([110, 30, 90])
    upper_fuchsia = np.array([180, 255, 255])
    lower_blue = np.array([85, 30, 190])
    upper_blue = np.array([125,255,255])

    # Aplicar mascaras para cada billete
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    fuchsia_mask = cv2.inRange(hsv, lower_fuchsia, upper_fuchsia)
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Contar el número de pixeles para cada billete
    green_pixels = cv2.countNonZero(green_mask)
    yellow_pixels = cv2.countNonZero(yellow_mask)
    fuchsia_pixels = cv2.countNonZero(fuchsia_mask)
    blue_pixels = cv2.countNonZero(blue_mask)

    # Determinar el billete con la mayor cantidad de pixeles
    max_pixels = max(green_pixels, yellow_pixels, fuchsia_pixels, blue_pixels)
    if max_pixels == green_pixels:
        return 10
    elif max_pixels == yellow_pixels:
        return 20
    elif max_pixels == fuchsia_pixels:
        return 50
    elif max_pixels == blue_pixels:
        return 100
    else:
        return "Billete no identificado"

imagen = cv2.imread("20old.jpg")
valor = detect_bill(imagen)
ventana = "VALOR DEL BILLETE: " + str(valor)
cv2.imshow(ventana, imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("El valor del billete es:", valor)