import cv2
import numpy as np
import matplotlib.pyplot as plt
import datetime
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

oldtime = datetime.datetime.now()  # 开始计时
def  hisg(img, level):
    gap = 256/level  #每个等级的大小
    x = np.arange(level)

    (B, G, R) = cv2.split(img)
    BGR = [B, G, R]
    size = img.shape
    scale = np.zeros((4, level))
    for j in range(3):
        for pixel in BGR[j].flat:
            for i in range(level):
                if (pixel>=gap*i and pixel<gap*(i+1) ):
                    scale[j, i] += 1
                    scale[3, i] += 1



    plt.subplot(2,2,1)
    plt.xlabel("R")
    plt.ylabel("出现次数")
    plt.title("R通道像素分布直方图")
    plt.plot(x, scale[2])

    plt.subplot(2, 2, 2)
    plt.xlabel("G")
    plt.ylabel("出现次数")
    plt.title("G通道像素分布直方图")
    plt.plot(x, scale[1])

    plt.subplot(2, 2, 3)
    plt.xlabel("B")
    plt.ylabel("出现次数")
    plt.title("B通道像素分布直方图")
    plt.plot(x, scale[0])

    plt.subplot(2, 2, 4)
    plt.xlabel("SUM")
    plt.ylabel("出现次数")
    plt.title("三通道像素分布直方图")
    plt.plot(x, scale[3])
    plt.show()

    newtime = datetime.datetime.now()  # 运算结束时间
    print("用时：{}微秒".format((newtime - oldtime).microseconds))

img = cv2.imread("bird2.jpg")
level = 10
hisg(img,level)
