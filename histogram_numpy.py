import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import datetime

img = cv2.imread("img1.jpg",0)


#numpy实现
old_time = datetime.datetime.now()  # 开始计时


def numpy_his(img,span):
    scale = np.zeros(256)
    for i in range (256):
        ncounts = img[img==i]  #表示截取矩阵中==i的元素
        if i==0 :
            scale[i] = (len(ncounts))
        else:
            scale[i] = sum(ncounts)/i
    level = np.empty((span,))
    x_ticks = math.ceil(256 / span)  # 设置x轴刻度
    for i in range(span):
        level[i] = sum(scale[i * x_ticks:(i + 1) * x_ticks])  # 根据所需要的跨距创造一个新的数组以画图
    plt.plot(np.linspace(0, 256, span), level)  # x定义为np.linspace(0, 256, span)
    plt.show()
    return level


hist = cv2.calcHist([img], [0], None, [10], [0, 256])
hist = np.resize(hist, (1, 10))
level = numpy_his(img, 10)
m = hist-level
m = np.square(m)
s = math.sqrt(sum(m.flat))


new_time = datetime.datetime.now()  #结束计时

print("用时：{}".format((new_time - old_time).microseconds))

#711794
