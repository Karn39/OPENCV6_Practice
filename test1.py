import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('Ch1.jpg')
head=img[150:577,378:750]
bb=img[100:527,100:472]
dst=cv2.addWeighted(bb,0.7,head,0.3,0)
img[100:527,100:472]=dst

cv2.imshow('res',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

''' gray 
grayImg=cv2.imread('Ch1.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('gray',grayImg)
'''