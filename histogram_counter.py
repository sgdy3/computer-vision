import cv2
import matplotlib.pyplot as plt
import datetime
import numpy as np
import math
from collections import Counter
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

old_time = datetime.datetime.now()  # 开始计时

def counter_his(img,span) :
    img = img.flat
    l_img = list(img)  #把矩阵化成counter可执行的list
    result = Counter(l_img)  ##获取每个pixel出现的次数，并保存在value中
    for key in range(256):
        result[key] = result.get(key, 0)  #对未出现的pixel补0
    scale = np.empty((256,))
    for i in range(256):
        scale[i] = result[i]   #字典按key的顺序转换为数组
    level = np.empty((span, ))
    x_ticks = math.ceil(256/span)  #设置x轴刻度,使用进一函数，因为参考cv2中函数进一而非四舍五入
    for i in range(span):
        level[i] = sum(scale[i*x_ticks:(i+1)*x_ticks])  #根据所需要的跨距创造一个新的数组以画图
    plt.plot(np.linspace(0, 256, span), level)  #x定义为np.linspace(0, 256, span)
    plt.show()
    return level

img = cv2.imread("img1.jpg",0)
level = counter_his(img,10)
new_time = datetime.datetime.now()   #结束计时

print("用时：{}".format((new_time - old_time).microseconds))

#234642

#完结，如果只是单纯的想要输出以0-256为x坐标的直方图完全不需要这么复杂
# 只需对函数中的result作bar图就可以，速度是当前的1/4左右

