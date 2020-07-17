import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('IMG_2917.jpg')
rows, cols, ch = img.shape

# 設置標記座標和目標座標 (左上右上左下右下)
markpoint = [[53, 1514], [1631, 905], [1037, 4029], [3023, 2682]]
dstpoint = [[0, 0], [3024, 0], [0, 4032], [3024, 4032]]

# 強調標記座標(上綠點)
for i in markpoint:
    cv2.circle(img, tuple(i), 10, (0, 255, 0), -1)

# 轉換座標格式
pts1 = np.float32(markpoint)
pts2 = np.float32(dstpoint)

# 生成透視矩陣
M = cv2.getPerspectiveTransform(pts1, pts2)

# 轉換
dst = cv2.warpPerspective(img, M, (3024, 4032))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
