import cv2
import numpy as np
import matplotlib.pyplot as plt
import datetime

img = cv2.imread(r'E:\python trial\python now\test\source\s1\10.png',0)

old_time1=datetime.datetime.now()
lut = np.zeros(256, dtype = img.dtype )#创建空的查找表
hist,bins = np.histogram(img.flat,256,[0,256])    #得到灰度分布列表
cdf = hist.cumsum() #  计算每个pixel对应的cdf值
cdf_m = np.ma.masked_equal(cdf,0) #消去cdf中的零值
# cdf_m = (cdf_m - 1)*255/(img.size-1) #求出均衡化之后的pixel值
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min()) #求出均衡化之后的pixel值
cdf = np.ma.filled(cdf_m,0).astype('uint8') #将之前出去的零值补回
result2 = cdf[img]  #以img中的每一个像素值为索引找到它变换之后的像素值
hist_1,bins_1 = np.histogram(result2.flat,256,[0,256])    #得到灰度分布列
new_time1=datetime.datetime.now()
# result = cv2.LUT(img, cdf)


#与自带函数进行比较
# old_time2=datetime.datetime.now()
# equ = cv2.equalizeHist(img)
# hist_2,bins_2= np.histogram(equ.flat,256,[0,256])
# new_time2=datetime.datetime.now()



x=np.arange(256)
plt.subplot(221)
plt.imshow(img,cmap="gray")
plt.subplot(222)
plt.bar(x,hist)
plt.subplot(223)
plt.imshow(result2,cmap="gray")
plt.subplot(224)
plt.bar(x,hist_1)
# plt.figure()
# plt.bar(x,hist_2)
plt.show()

print((new_time1-old_time1).microseconds)
# print((new_time2-old_time2).microseconds)

