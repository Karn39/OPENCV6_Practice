import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('Ch1.jpg')
head=img[150:577,378:750]
bb=img[100:527,100:472]
dst=cv2.addWeighted(bb,0.7,head,0.3,0)
#grayImg=cv2.imread('Ch1.jpg')
print(img)

cv2.imshow('res',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()