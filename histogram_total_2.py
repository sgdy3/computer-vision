import cv2
import matplotlib.pyplot as plt
import datetime
import numpy as np
import math
from collections import Counter

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

def minus(array_1,array_2):
    m = array_1 - array_2
    m = np.square(m)
    s = math.sqrt(sum(m.flat))
    return s
img = cv2.imread(r'E:\python trial\python now\test\source\s1\1.pgm',0)

old_time_0= datetime.datetime.now()  # 开始计时
hist_0 = dict_his(img, 256)  #将dict换成numpy,counter以更换函数
new_time_0 = datetime.datetime.now()  #结束计时

old_time_1 = datetime.datetime.now()  # 开始计时
hist_1 = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist_1)
plt.show()
new_time_1 = datetime.datetime.now()  #结束计时
hist_1 = np.resize(hist_1, (1, 256))
sum_1= minus(hist_0, hist_1)

old_time_2 = datetime.datetime.now()  # 开始计时
arr = img.flatten()
hist_2, bins, patches = plt.hist(arr, bins=256)
plt.show()
new_time_2 = datetime.datetime.now()  #结束计时
hist_1 = np.resize(hist_2, (1, 256))
sum_2= minus(hist_0, hist_2)

old_time_3 = datetime.datetime.now()  # 开始计时
hist_3,b = np.histogram(img, bins=256, range=(0, 256))
plt.plot(hist_3)
plt.show()
new_time_3 = datetime.datetime.now()  #结束计时
hist_1 = np.resize(hist_3, (1, 256))
sum_3= minus(hist_0, hist_3)





print("用时：{}".format((new_time_0 - old_time_0).microseconds))
print("用时：{}".format((new_time_1 - old_time_1).microseconds))
print("用时：{}".format((new_time_2 - old_time_2).microseconds))
print("用时：{}".format((new_time_3 - old_time_3).microseconds))