import cv2

cap = cv2.VideoCapture(0)
fps = 23.0  #设置帧数
time = 5*fps  #设置录制时间

size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc(*'MPEG')  #写入fourcc
out = cv2.VideoWriter('cvcourse.avi', fourcc, fps, size)

while(cap.isOpened() and time>0):#拍摄5s后关闭
    ret, frame = cap.read()
    if ret==True:
        out.write(frame)
        time -=1
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  #按下q关闭
            break
    else:
        break


#关闭窗口
cap.release()
out.release()
cv2.destroyAllWindows()


