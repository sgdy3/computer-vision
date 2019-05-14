import numpy as np
import cv2
import matplotlib.pyplot as plt
import datetime
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
from collections import Counter


img = cv2.imread("img1.jpg",0)


#numpy实现
oldtime_1 = datetime.datetime.now()  # 开始计时
scale = np.zeros(256)
for i in range (256):
    ncounts = img[img==i]  #表是截取矩阵中==i的元素
    if i==0 :
        scale[i] = (len(ncounts))
    else:
        scale[i] = sum(ncounts)/i
plt.title("numpy实现")
plt.subplot(2,2,1)
plt.plot(scale)
newtime_1 = datetime.datetime.now()  # 运算结束时间

oldtime_2 = datetime.datetime.now()  # 开始计时
hist = cv2.calcHist([img],[0],None,[256],[0,256])

plt.subplot(2,2,2)#新建一个图像
plt.title("Grayscale Histogram")#图像的标题
plt.xlabel("Bins")#X轴标签
plt.ylabel("# of Pixels")#Y轴标签
plt.plot(hist)#画图
plt.xlim([-25,256])#设置x坐标轴范围
newtime_2 = datetime.datetime.now()  # 运算结束时间


#通过遍历字典输出
#先尝试了对字典返回值按key进行排序，1：直接用sort函数只返回了key的值，想以此遍历value失败。
#2：按key排序返回含元组的列表，画图失败，不能将其转化为dict或列表
#3：发现不用给value排序，是画图时x轴的问题,因为画折线图时每两个点就连一条线，而数据无序，连线也就无序，未解决


oldtime_4 = datetime.datetime.now()  # 开始计时
v = list(img)
result = Counter((v))
plt.subplot(2,2,4)
plt.title("counter实现")
plt.plot(result.keys(),result.values())
newtime_4 = datetime.datetime.now()  # 运算结束时间

oldtime_3 = datetime.datetime.now()  # 开始计时
dict = {}
for key in img:
    dict[key] = dict.get(key, 0) + 1
for key in range(256):
    dict[key] = dict.get(key, 0)
x = list(dict.keys())
y = list(dict.values())
plt.subplot(2,2,3)
plt.title("字典实现")
plt.bar(x,y)
newtime_3 = datetime.datetime.now()  # 运算结束时间



plt.show()

print("numpy用时：{}微秒".format((newtime_1 - oldtime_1).microseconds))
print("cv2用时：{}微秒".format((newtime_2 - oldtime_2).microseconds))
print("字典用时：{}微秒".format((newtime_3 - oldtime_3).microseconds))
print("counter用时：{}微秒".format((newtime_4 - oldtime_4).microseconds))






