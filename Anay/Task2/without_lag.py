import cv2
import numpy
import datetime
import time
cap=cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
#w=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
#h=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
#w,h=map(int,[w,h])
#print(fps,(w,h))

cap.set(3,160)
cap.set(4,120)
saved=cv2.VideoWriter('saved_video.avi',cv2.VideoWriter_fourcc(*'MJPG'),fps,(160,120))
startT = datetime.datetime.now()
while cap.isOpened() :

    check,frame=cap.read()
    currentT = datetime.datetime.now()
    if ((currentT-startT).total_seconds())>5.27: #due to the start delay of camera capturing starts around .26 seconds
        break
    #print((currentT-startT).total_seconds())

    if check:
        cv2.imshow('capturing',frame)
        saved.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
saved.release()

cv2.destroyAllWindows()
