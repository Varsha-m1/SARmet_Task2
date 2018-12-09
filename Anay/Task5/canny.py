import numpy as np
import cv2
import imutils

img = cv2.imread('720x1280.jpg')
img=imutils.resize(img,width=400)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#blur = cv2.GaussianBlur(gray, (3, 3), 0)

m = np.median(img)
#print(m)
lower = int(max(0,(1.0-0.33) * m))
upper = int(min(255,(1.0+0.33) * m))
#print(lower,upper)
edged = cv2.Canny(img, lower, upper,apertureSize=3,L2gradient=True)

cv2.imshow("Original", img)
cv2.imshow("Edges",edged)
cv2.imwrite('image.jpg',edged)
cv2.waitKey(0)
