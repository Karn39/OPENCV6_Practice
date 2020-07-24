import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./trainImg/0.0001.jpg', 0)
blur = cv2.blur(img,(15,15))

edges = cv2.Canny(blur, 10, 50)
edges2 = cv2.Canny(blur, 30, 80)
edges3 = cv2.Canny(blur, 30, 85)
edges4 = cv2.Canny(blur, 30, 90)
edges5 = cv2.Canny(blur, 10, 120)

plt.subplot(231), plt.imshow(blur, cmap='gray'), plt.title('Original Image')
plt.subplot(232), plt.imshow(edges, cmap='gray'), plt.title('Edge Image')
plt.subplot(233), plt.imshow(edges2, cmap='gray'), plt.title('Edge2 Image')
plt.subplot(234), plt.imshow(edges3, cmap='gray'), plt.title('Edge3 Image')
plt.subplot(235), plt.imshow(edges4, cmap='gray'), plt.title('Edge4 Image')
plt.subplot(236), plt.imshow(edges5, cmap='gray'), plt.title('Edge5 Image')

plt.show()