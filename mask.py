import cv2
import numpy as np

img = cv2.imread('./trainImg/0.0001.jpg', cv2.IMREAD_COLOR)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
color = np.uint8([[[53,51,43]]])
hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
print(hsv_color)

lower_red_0 = np.uint8([100,45,35]) 
upper_red_0 = np.uint8([100 + 20,45 + 20,35 + 20])
lower_red_1 = np.uint8([100 , 45 , 35]) 
upper_red_1 = np.uint8([100 + 50, 45 + 50, 35 + 50])
red_mask0 = cv2.inRange(hsv_img, lower_red_0, upper_red_0)
red_mask1 = cv2.inRange(hsv_img, lower_red_1, upper_red_1)
red_mask = cv2.bitwise_or(red_mask0, red_mask1) 

cv2.imshow("red_mask", red_mask1) 
cv2.imshow("test", img)
cv2.waitKey(0)