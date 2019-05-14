import numpy as np
import cv2

cap = cv2.VideoCapture(0) #参数选择0即指向第一个摄像头

while(True):
    # 截取帧，ret为bool型，表征是否截取成功，frame为截取到的图片
    ret, frame = cap.read()
    if(ret):
        # 显示截取的帧
        cv2.imshow('frame', frame)
    else:
        print("调用摄像头失败")
        break
    if cv2.waitKey(1000) & 0xFF == ord('q'):  #waitKey(1) 中的数字代表等待按键输入之前的无效时间，单位为毫秒，在这个时间段内按键 ‘q’ 不会被记录
        cv2.imwrite('last frame.jpg',frame)
        break
#waitKey(1) 中的数字代表等待按键输入之前的无效时间，单位为毫秒，在这个时间段内按键 ‘q’ 不会被记录，waitkey返回值即键盘输入值
#在这之后按键才会被记录，并在下一次进入if语段时起作用。也即经过无效时间以后，检测在上一次显示图像的时间段内按键 ‘q’ 有没有被按下，若无则跳出if语句段，捕获并显示下一帧图像。
# cv2.waitKey(1000)
# local_cap = cv2.VideoCapture('output.avi')
# print(local_cap.get(cv2.CAP_PROP_FPS))
# print(local_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# print(local_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# while(local_cap.isOpened()):
#     ret, frame = local_cap.read()
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(50) & 0xFF == ord('q'):
#         break


# 关闭窗口，释放空间
cap.release()
cv2.destroyAllWindows()