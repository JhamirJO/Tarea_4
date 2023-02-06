import cv2

from matplotlib import pyplot as plt

img = cv2.imread('prueba.png', 0)


hist = cv2.calcHist([img], [0], None, [256], [0, 256])

fig, ax = plt.subplots(2, 2)
ax[0, 0].imshow(img, cmap='gray')
ax[0, 0].set_title('Imagen')
ax[0, 0].axis('off')

ax[0, 1].plot(hist, color='gray')
ax[0, 1].set_title('Histograma')

ax[1, 0].imshow(img, cmap='gray')
ax[1, 0].set_title('Imagen')
ax[1, 0].axis('off')

ax[1, 1].hist(img.ravel(), 256, [0, 256])

plt.show()



cv2.waitKey(0)
cv2.destroyAllWindows()