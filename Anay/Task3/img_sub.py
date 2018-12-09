import cv2
import numpy

img=cv2.imread('720x1280.jpg',1)

flip_x=cv2.flip(img,0)
cv2.imwrite('flip_x.png',flip_x)
flip_y=cv2.flip(img,1)
cv2.imwrite('flip_y.png',flip_y)

sub=cv2.subtract(flip_x,flip_y)
cv2.imwrite('subtracted_image.png',sub)

cv2.imshow('sub',sub)
if cv2.waitKey(5000):
    cv2.destroyAllWindows()
