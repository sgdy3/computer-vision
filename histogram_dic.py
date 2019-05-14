import numpy as np
import cv2
import matplotlib.pyplot as plt
import datetime
import math
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签



def dict_his(img,span):
    img = img.flat
    dict = {}
    for key in img:
        dict[key] = dict.get(key, 0) + 1
    for key in range(256):
        dict[key] = dict.get(key, 0)
    scale = np.empty((256,))
    for i in range(256):
        scale[i] = dict[i]   #字典按key的顺序转换为数组
    level = np.empty((span, ))
    x_ticks = math.ceil(256/span)  #设置x轴刻度
    for i in range(span):
            level[i] = sum(scale[i*x_ticks:(i+1)*x_ticks])  #根据所需要的跨距创造一个新的数组以画图
    plt.plot(np.linspace(0, 256, span), level)  #x定义为np.linspace(0, 256, span)
    plt.show()
    return level


img = cv2.imread("img1.jpg",0)
old_time = datetime.datetime.now()  # 开始计时
level = dict_his(img, 10)
hist = cv2.calcHist([img], [0], None, [10], [0, 256])
plt.plot(hist)
plt.show()
new_time = datetime.datetime.now()  #结束计时

print("用时：{}".format((new_time - old_time).microseconds))

#675563
