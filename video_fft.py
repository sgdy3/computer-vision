import cv2
import numpy as np
from matplotlib import pyplot as plt

img_man = cv2.imread(r'E:\python trial\python now\test\picture\assassin.jpeg',0) #直接读为灰度图像
height,width = img_man.shape
plt.subplot(321),plt.imshow(img_man,"gray"),plt.title('origial')
plt.xticks([]),plt.yticks([])
#--------------------------------
#创造四个蒙版分别对应60%， 30%， 10%， 1%频谱范围
rows,cols = img_man.shape
rows,cols=np.ceil(rows/2),np.ceil(cols/2)
rows,cols=np.int(rows),np.int(cols)
mask_1=np.zeros(img_man.shape,np.uint8)
mask_2=np.zeros(img_man.shape,np.uint8)
mask_3=np.zeros(img_man.shape,np.uint8)
mask_4=np.zeros(img_man.shape,np.uint8)
mask_1[(rows-int(height*0.005)):(rows+int(height*0.005)), (cols-int(width*0.005)):(cols+int(width*0.005))] = 1
mask_2[(rows-int(height*0.05)):(rows+int(height*0.05)), (cols-int(width*0.05)):(cols+int(width*0.05))] = 1
mask_3[(rows-int(height*0.15)):(rows+int(height*0.15)), (cols-int(width*0.15)):(cols+int(width*0.15))] = 1
mask_4[(rows-int(height*0.3)):(rows+int(height*0.3)), (cols-int(width*0.3)):(cols+int(width*0.3))] = 1
#--------------------------------
mask_t=[mask_1,mask_2,mask_3,mask_4]
title=["1%", "10%", "30%", "60%"]
ang=322

f1 = np.fft.fft2(img_man)
f1shift = np.fft.fftshift(f1)
for i in range(4):
        #对原图片频谱进行截取操作
        f1_shift = f1shift * mask_t[i]
        f2shift = np.fft.ifftshift(f1_shift)  # 对新的矩阵进行逆变换
        img_new = np.fft.ifft2(f2shift)
        #取频谱元素的绝对值，即图像灰度信息
        img_new = np.abs(img_new)
        # 调整大小范围便于显示
        # img_new = (img_new - np.amin(img_new)) / (np.amax(img_new) - np.amin(img_new))
        plt.subplot(ang), plt.imshow(img_new, 'gray'), plt.title(title[i])
        plt.xticks([]), plt.yticks([])
        ang=ang+1  #使图片能够按顺序出现在底板上
plt.show()
