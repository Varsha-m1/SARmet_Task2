#Setting L2Gradient field
import cv2
img = cv2.imread("720x1280.jpg")
img1 = cv2.Canny(img,100,200,True)
cv2.imwrite('L2Gradient.jpg',img1)

#Changing Sobel Apertures
import cv2
img = cv2.imread("720x1280.jpg")
img1 = cv2.Canny(img,100,200,1)
cv2.imwrite('SobelAperture1.jpg',img1)
