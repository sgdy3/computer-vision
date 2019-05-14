import cv2
import numpy as np
import matplotlib.pyplot as plt

# 卷积
def imgConvolve(image, kernel):
    '''
    :param image: 图片矩阵
    :param kernel: 滤波窗口
    :return:卷积后的矩阵
    '''
    img_h = int(image.shape[0])
    img_w = int(image.shape[1])
    kernel_h = int(kernel.shape[0])
    kernel_w = int(kernel.shape[1])
    # padding
    padding_h = int((kernel_h - 1) / 2)
    padding_w = int((kernel_w - 1) / 2)

    convolve_h = int(img_h + 2 * padding_h)
    convolve_W = int(img_w + 2 * padding_w)

    # 分配空间
    img_padding = np.zeros((convolve_h, convolve_W))
    # 中心填充图片
    img_padding[padding_h:padding_h + img_h, padding_w:padding_w + img_w] = image[:, :]
    # 卷积结果
    image_convolve = np.zeros(image.shape)
    # 卷积
    for i in range(padding_h, padding_h + img_h):
        for j in range(padding_w, padding_w + img_w):
            image_convolve[i - padding_h][j - padding_w] = int(
                np.sum(img_padding[i - padding_h:i + padding_h+1, j - padding_w:j + padding_w+1]*kernel))
    return image_convolve
# 高斯滤波
def imgGaussian(sigma):
    '''
    :param sigma: σ标准差
    :return: 高斯滤波器的模板
    '''
    img_h = img_w = 2 * sigma + 1
    gaussian_mat = np.zeros((img_h, img_w))
    for x in range(-sigma, sigma + 1):
        for y in range(-sigma, sigma + 1):
            gaussian_mat[x + sigma][y + sigma] = np.exp(-0.5 * (x ** 2 + y ** 2) / (sigma ** 2))
    return gaussian_mat

img = cv2.imread(r'E:\python trial\python now\test\picture\lena.png',0)
gaussian_mat=imgGaussian(10)
# kernel=np.array([[1,2,1],[2,4,2],[1,2,1]])
img_new=imgConvolve(img,gaussian_mat)
plt.subplot(121)
plt.title("previous")
plt.imshow(img,cmap="gray")
plt.subplot(122)
plt.title("transform")
plt.imshow(img_new,cmap="gray")
plt.show()
cv2.imshow("pre",img)
cv2.imshow("now",img_new)
cv2.waitKey(0)

