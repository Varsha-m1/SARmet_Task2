import cv2
import numpy as np
#import imutils

img=cv2.imread('720x1280.jpg',1)

img=img[:240,:]
cv2.imshow('cropped',img)

m = np.median(img)
#print(m)
lower = int(max(0,(1.0-0.33) * m))
upper = int(min(255,(1.0+0.33) * m))
#print(lower,upper)
edged = cv2.Canny(img, lower, upper)

cv2.imshow('edge_detected',edged)
cv2.imwrite('edge_detected.jpg',edged)

if cv2.waitKey(0):
    cv2.destroyAllWindows()
