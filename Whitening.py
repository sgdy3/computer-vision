import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
import datetime

img = cv2.imread(r'E:\python trial\python now\test\source\s1\10.png',0)
old_time= datetime.datetime.now()
height,width = img.shape
mean = np.sum(img)/(height*width)  #求均值
a = (img-mean)**2  #（pij-mean）2
var=math.sqrt(np.sum(a)/(height*width))  #求标准差
img_1= (img-mean)/var
minus = np.max(img_1)-np.min(img_1)
img_1 = 255*(img_1-np.min(img_1))/(minus)
img_1=img_1.astype("uint8")
new_time=datetime.datetime.now()
print((new_time-old_time).microseconds)


plt.subplot(221)
plt.title("previous")
a_1=cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(a_1)
plt.subplot(222)
plt.imshow(img,cmap="gray")
plt.subplot(223)
plt.title("now")
a_2=cv2.calcHist([img_1], [0], None, [256], [0, 256])
plt.plot(a_2)
plt.subplot(224)
plt.imshow(img_1,cmap="gray")
plt.show()
# cv2.imshow("0",img)
# cv2.imshow("1",img_1)
# cv2.imwrite('now.png',img_1)
# cv2.waitKey(0)


# # img_2 = img_1**2
# # img_3 = img_2/(height*width)
# img_2=(img-equal_mat)/var
#（b-a)*(xij-min)/(max-min)
