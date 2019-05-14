import numpy as np
import cv2

img = cv2.imread("assassin.jpeg")
#彩色图像分离为三通道
B, G, R = cv2.split(img)
#补充为0的维度
zeros = np.zeros(img.shape[:2], dtype = "uint8")
#三通道升维
B = cv2.merge([B, zeros, zeros])
G = cv2.merge([zeros, G, zeros])
R = cv2.merge([zeros, zeros, R])
#显示三个通道的图片
cv2.imshow("Blue", B)
cv2.imshow("Green", G)
cv2.imshow("Red", R)
#保存三个通道的图片
cv2.imwrite("assassin_B_95.jpg", B)
cv2.imwrite("assassin_G.jpg", G)
cv2.imwrite("assassin_R.jpg", R)
#以蓝色通道为例，比较不同保存方式对图像质量等方面的影响
cv2.imwrite("assassin_B_5.jpg", B, [int(cv2.IMWRITE_JPEG_QUALITY), 5])
cv2.imwrite("assassin_B_9.png", B, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
cv2.imwrite("assassin_B_3.png", B)
cv2.imwrite("assassin_B.tiff",B)
cv2.imwrite("assassin_B.bmp", B)

cv2.waitKey()
