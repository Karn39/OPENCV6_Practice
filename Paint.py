import numpy as np
import cv2

# Create a black image
img=np.zeros((512,512,3),np.uint8)

#Draw a diagonal blue line with thickness of 5px
#cv2.line(img,(0,0),(511,511),(255,0,0),5)
#Draw a green square 左上角與右下角座標、線條粗度
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
#Draw a red circle 圓心座標、半徑、線條粗度(-1為填滿)
cv2.circle(img,(447,63),63,(0,0,255),-1)
#Draw a ellipse 圓心座標、長軸與短軸長度、逆時針旋轉、順時針旋轉、圓度
cv2.ellipse(img,(256,256),(100,50),0,0,360,255,-1)
#Add Text 文字、位置、字體、字體大小、顏色、文字粗細
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Chihuahua',(10,500),font,2,(255,255,255),4)

cv2.imshow('Paint',img)
cv2.waitKey(0)
cv2.destroyAllWindows()