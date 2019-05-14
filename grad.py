import cv2
import numpy as np
import matplotlib.pyplot as plt
import datetime

img = cv2.imread(r'E:\python trial\python now\test\source\s1\1.pgm',0)
old_time=datetime.datetime.now()

row, column = img.shape
img_f = np.copy(img)
img_f= img_f.astype(int)   #将图片中数据类型改为int,否在会在减法操作中出现超出范围错误
gradient = np.zeros((row, column),dtype="uint8")

for x in range(row - 1):
    for y in range(column - 1):
        gx = abs(img_f[x + 1, y] - img_f[x, y]) #求得每一个像素在其x方向上的梯度
        gy = abs(img_f[x, y + 1] - img_f[x, y])  #求得在y方向上的梯度
        gradient[x, y] = gx + gy    #用x,y方向上梯度的绝对值之和近似二者平方平均数

sharp = img_f + gradient   #得到梯度滤波化之后图片
sharp = np.where(sharp < 0, 0, np.where(sharp > 255, 255, sharp))   #np加法为模操作需将超出0～255的像素值拉回范围之内
sharp = sharp.astype("uint8")   #类型调回unit8
new_time=datetime.datetime.now()

plt.subplot(121)
plt.title("previous")
plt.imshow(img,cmap='gray')
# plt.subplot(122)
# plt.title("grad")
# plt.imshow(gradient,cmap='gray')
plt.subplot(122)
plt.title("now")
plt.imshow(sharp,cmap='gray')
plt.show()
print((new_time-old_time).microseconds)
