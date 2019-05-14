import cv2
import matplotlib.pyplot as plt
import datetime
import numpy as np
import math



img = cv2.imread("img1.jpg",0)

hist_3,b = np.histogram(img, bins=256, range=(0, 256))
plt.plot(hist_3)
plt.show()

