import cv2
import matplotlib.pyplot as plt

img2 = cv2.imread('prueba.png', cv2.IMREAD_COLOR)

img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

plt.imshow(img2, cmap="gray")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()