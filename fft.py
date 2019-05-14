import cv2
import numpy as np
import matplotlib.pyplot as plt

#以下为输出傅里叶变化后，原图，复数图，逆变换图
# img = cv2.imread('assassin.jpeg',0) #直接读为灰度图像
# f = np.fft.fft2(img)
# fshift = np.fft.fftshift(f)
# #取绝对值：将复数变化成实数
# #取对数的目的为了将数据变化到0-255
# s1 = np.log(np.abs(fshift))
# plt.subplot(131),plt.imshow(img,'gray'),plt.title('original')
# plt.subplot(132),plt.imshow(s1,'gray'),plt.title('center')
# # 逆变换
# f1shift = np.fft.ifftshift(fshift)
# img_back = np.fft.ifft2(f1shift)
# #出来的是复数，无法显示
# img_back = np.abs(img_back)
# plt.subplot(133),plt.imshow(img_back,'gray'),plt.title('img back')
# plt.show()
# print("down")

# img1=cv2.imread('assassin.jpeg',0)
# f=np.fft.fft2(img1)
# fshift=np.fft.fftshift(f)
# rows,cols=img1.shape
# crow,ccol=np.ceil(rows/2),np.ceil(cols/2)
# crow,ccol=np.int(crow),np.int(ccol)
# #注意fshift是用来与原图像进行掩模操作的但是具体的，我也看着很抽象。这一部分与低通的有些相对的意思。
# fshift[crow-30:crow+30,ccol-30:ccol+30]=0   #截取直流部分的数据并将其变为0
# f_ishift=np.fft.ifftshift(fshift)
# img_back=np.fft.ifft2(fshift)
# img_back=np.abs(img_back)
# plt.subplot(1,2,1),plt.imshow(img1,'gray')
# plt.title('input image'),plt.xticks([]),plt.yticks([])
# plt.subplot(1,2,2),plt.imshow(img_back)
# plt.title('image after HPF'),plt.xticks([]),plt.yticks([])
# plt.show()


#傅里叶变换实现
# img1=cv2.imread('assassin.jpeg',0)
# dft=cv2.dft(np.float32(img1),flags=cv2.DFT_COMPLEX_OUTPUT)
# dft_shift=np.fft.fftshift(dft)
# magnitude_spectrum=20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
# rows,cols=img1.shape
# #下面有对数据的取整还有数据类型转换的操作，否则mask会出问题
# crow,ccol=np.ceil(rows/2),np.ceil(cols/2)
# crow,ccol=np.int(crow),np.int(ccol)
# mask=np.zeros((rows,cols,2),np.uint8)
# mask[crow-30:crow+30,ccol-30:ccol+30]=1
# fshift=dft_shift*mask
# f_ishift=np.fft.ifftshift(fshift)
# img_back=cv2.idft(f_ishift)
# img_back=cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
# plt.subplot(1,2,1),plt.imshow(img1)
# plt.title('input image'),plt.xticks([]),plt.yticks([])
# plt.subplot(1,2,2),plt.imshow(img_back)
# plt.title('magnitude spectrum'),plt.xticks([]),plt.yticks([])
# plt.show()





img_man = cv2.imread('assassin.jpeg',0) #直接读为灰度图像
height,width = img_man.shape
plt.subplot(221),plt.imshow(img_man,"gray"),plt.title('origial')
plt.xticks([]),plt.yticks([])
#--------------------------------
rows,cols = img_man.shape
rows,cols=np.ceil(rows/2),np.ceil(cols/2)
rows,cols=np.int(rows),np.int(cols)
mask_1 = np.zeros(img_man.shape,np.uint8)
mask_2 = np.zeros(img_man.shape,np.uint8)
mask_3 = np.zeros(img_man.shape,np.uint8)
mask_1[(rows-int(height*0.005)):(rows+int(height*0.005)), (cols-int(width*0.005)):(cols+int(width*0.005))] = 1
mask_2[(rows-int(height*0.05)):(rows+int(height*0.05)), (cols-int(width*0.05)):(cols+int(width*0.05))] = 1
mask_3[(rows-int(height*0.3)):(rows+int(height*0.3)), (cols-int(width*0.3)):(cols+int(width*0.3))] = 1
#--------------------------------
# f1 = np.fft.fft2(img_man)
# # f1shift = np.fft.fftshift(f1)
# # f1shift = f1shift*mask_1
# # f2shift = np.fft.ifftshift(f1shift) #对新的进行逆变换
# # img_new = np.fft.ifft2(f2shift)
# # #出来的是复数，无法显示
# # img_new = np.abs(img_new)
# # #调整大小范围便于显示
# # img_new = (img_new-np.amin(img_new))/(np.amax(img_new)-np.amin(img_new))
# # plt.subplot(222),plt.imshow(img_new,'gray'),plt.title('Highpass')
# # plt.xticks([]),plt.yticks([])
# # plt.show()

mask_t=[mask_1,mask_2,mask_3]
ang=222
for item in mask_t:
    f1 = np.fft.fft2(img_man)
    f1shift = np.fft.fftshift(f1)
    f1shift = f1shift * item
    f2shift = np.fft.ifftshift(f1shift)  # 对新的进行逆变换
    img_new = np.fft.ifft2(f2shift)
    # 出来的是复数，无法显示
    img_new = np.abs(img_new)
    # 调整大小范围便于显示
    img_new = (img_new - np.amin(img_new)) / (np.amax(img_new) - np.amin(img_new))
    plt.subplot(ang), plt.imshow(img_new, 'gray'), plt.title('fft')
    plt.xticks([]), plt.yticks([])
    ang=ang+1
plt.show()

