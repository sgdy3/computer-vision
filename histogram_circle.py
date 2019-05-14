import cv2
import numpy as np
import matplotlib.pyplot as plt
import datetime
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

oldtime=datetime.datetime.now()  #开始计时
img = cv2.imread("bird2.jpg")
(B, G, R) = cv2.split(img)
BGR = [B,G,R]
size = img.shape
scale = np.zeros((4, 256))
for j in range(3):
    for pixel in BGR[j].flat :
        for i in range(256):
            if pixel == i :
                scale[j,i] +=1
                scale[3,i] +=1

x = np.arange(256)

plt.subplot(2, 2, 1)
plt.xlabel("R")
plt.ylabel("出现次数")
plt.title("R通道像素分布直方图")
plt.plot(x,scale[2])


plt.subplot(2, 2, 2)
plt.xlabel("G")
plt.ylabel("出现次数")
plt.title("G通道像素分布直方图")
plt.plot(x,scale[1])


plt.subplot(2, 2, 3)
plt.xlabel("B")
plt.ylabel("出现次数")
plt.title("B通道像素分布直方图")
plt.plot(x,scale[0])


plt.subplot(2, 2, 4)
plt.xlabel("SUM")
plt.ylabel("出现次数")
plt.title("三通道像素分布直方图")
plt.plot(x,scale[3])
plt.show()

newtime=datetime.datetime.now()  #运算结束时间

chans = cv2.split(img)
colors = ("b","g","r")

for (chan,color) in zip(chans,colors):
    plt.figure()
    plt.title("像素分布直方图——cv2")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    hist = cv2.calcHist([chan],[0],None,[256],[0,256])
    plt.plot(hist,color = color)
    plt.xlim([-20,256])
    plt.show()

for (chan,color) in zip(chans,colors):
    arr = chan.flatten()
    plt.title("像素分布直方图——matplotlib")  # 图像的标题
    n, bins, patches = plt.hist(arr, bins=256, normed=0, facecolor=color, alpha=0.75)
    plt.show()



print("用时：{}微秒".format((newtime-oldtime).microseconds))





# zeros = np.zeros(img.shape[:2], dtype = "uint8")
# cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
# cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
# cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
# cv2.waitKey()