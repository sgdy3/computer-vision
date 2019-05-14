import cv2
import numpy as np
import matplotlib.pyplot as plt
import datetime


#卷积运算
def imgconvolve(img ,kernel):
    img_h,img_w=img.shape
    kernel_h,kernel_w=kernel.shape
    img_conv=np.zeros((img_h,img_w))
    #————————————————————
    #以0填充边界，使边界的元素也可以进行卷积运算，得到新的底
    img_new=np.zeros((img_h+kernel_h-1,img_w+kernel_w-1))
    up=int((kernel_h-1)/2)
    down=int((kernel_h-1)/2+img_h)
    left=int((kernel_w-1)/2)
    right=int((kernel_w-1)/2+img_w)
    img_new[up:down,left:right]=img[:,:]
    #——————————————————
    #用循环进行卷积运算
    for i in range(up,down):
        for j in range(left,right):
            img_conv[i-up,j-left]=int(np.average(img_new[i-up:i+up+1,j-left:j+left+1]*kernel))
    #———————————————————
    #截取源图像大小部分
    img_conv=img_conv.astype("uint8")
    return img_conv
# 高斯滤波
def imgGaussian(sigma):
    '''
    :param sigma: σ标准差
    :return: 高斯滤波器的模板
    '''
    img_h = img_w = 2 * sigma + 1  #计算卷积核大小
    gaussian_mat = np.zeros((img_h, img_w))
    for x in range(-sigma, sigma + 1):
        for y in range(-sigma, sigma + 1):
            gaussian_mat[x + sigma][y + sigma] = np.exp(-0.5 * (x ** 2 + y ** 2) / (sigma ** 2))
    return gaussian_mat

img = cv2.imread(r'E:\python trial\python now\test\picture\lena.png',0)

old_time1=datetime.datetime.now()
gaussian_mat=imgGaussian(1)
# kernel=np.array([[1,2,1],[2,4,2],[1,2,1]])
img_conv=imgconvolve(img,gaussian_mat)
new_time1=datetime.datetime.now()
hist_1,bar_1=np.histogram(img_conv,256,[0,256])



old_time2=datetime.datetime.now()
blurred =cv2.GaussianBlur(img,(3,3),1)
new_time2=datetime.datetime.now()
hist_2,bar_2=np.histogram(blurred,256,[0,256])


plt.subplot(121)
plt.title("previous")
plt.imshow(img,cmap="gray")
plt.subplot(122)
plt.title("transform")
plt.imshow(img_conv,cmap="gray")
plt.show()

plt.figure()
plt.subplot(121)
plt.title("diy")
plt.plot(hist_1)
plt.subplot(122)
plt.title('cv2')
plt.plot(hist_2)
plt.show()
print((new_time1-old_time1).microseconds)
print((new_time2-old_time1).microseconds)




