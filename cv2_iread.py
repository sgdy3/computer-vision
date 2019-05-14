
"""
import numpy as np
import cv2

a = np.arange(30)
a = a.reshape((2, 5, 3))

print(a[:, :, 0])
print(a[:, :, 1])
print(a[:, :, 2])
"""
import cv2
img = cv2.imread (r'C:\Users\sgdy3\Videos\Gu jian 3\Gu jian 3 Screenshot 2019.02.15 - 14.52.24.06.png',0)
cv2.imshow('image',img)
cv2.imwrite("img1.tiff",img)
cv2.waitKey()





