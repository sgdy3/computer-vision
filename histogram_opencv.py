import cv2
import matplotlib.pyplot as plt

img = cv2.imread("assassin.jpeg")

chans = cv2.split(img)
colors = ("b","g","r")
hist = []
plt.figure()

for (chan, color) in zip(chans, colors):  #遍历三通道
    hist = cv2.calcHist([chan], [0], None, [10], [0, 256])
    plt.title("%s color histogram" %color)  #由%构成的可变title
    plt.plot(hist, color=color)  #因为color命名时恰好是color参数，直接使用
    plt.show()
