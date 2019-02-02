import cv2
import time

duration = 4
vidcap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'DVIX')
out = cv2.VideoWriter('videonew.mp4',fourcc, 20.0, (640,480))
a = time.time()
while int(time.time()-a)<duration:
    
    success,image = vidcap.read()
    print(success)
    cv2.imshow('Capturing', image)
    out.write(image)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break
vidcap.release()
vidcap.release()
cv2.destroyAllWindows()
