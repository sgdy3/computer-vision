import cv2
import numpy as np

img = np.array([
                [[255, 0, 0], [0, 255, 0]],
                [[0, 0, 255], [255, 255, 255]]
                ], dtype=np.uint8)
cv2.imwrite("test2.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
img = cv2.resize(img, (200, 200))
cv2.imshow("test",img)
cv2.waitKey()

