'''
19年3月27日
编码输出图片直方图
'''

import numpy as np
import cv2
import matplotlib.pyplot as plt
import datetime

img = cv2.imread("img1.jpg", 0)   #读取图片

old_time = datetime.datetime.now()  # 开始计时
scale = np.zeros(256)
x=np.arange(256)
for k in img.flat:
    for l in range(256):
        if (k == l):
            scale[l] +=1
plt.plot(x,scale)
plt.show()

new_time = datetime.datetime.now()  #结束计时

print("用时：{}".format((new_time - old_time).seconds))

#524s

#以下为复制而来
# hist = cv2.calcHist([img],[0],None,[256],[0,256])
#
# plt.figure()#新建一个图像
# plt.title("Grayscale Histogram")#图像的标题
# plt.xlabel("Bins")#X轴标签
# plt.ylabel("# of Pixels")#Y轴标签
# plt.plot(hist)#画图
# plt.xlim([-25,256])#设置x坐标轴范围
# plt.show()#显示图像
#
#
# arr=img.flatten()
# plt.title("matGrayscale Histogram")#图像的标题
# n, bins, patches = plt.hist(arr, bins=256, normed=0, facecolor='green', alpha=0.75)
# plt.show()












