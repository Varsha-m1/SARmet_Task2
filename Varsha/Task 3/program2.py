import cv2
img = cv2.imread("720x1280.jpg")
horizontal_img = img.copy()
vertical_img = img.copy()
horizontal_img = cv2.flip( img, 0 )#x-axis
vertical_img = cv2.flip( img, 1 )#y-axis
cv2.imwrite( "Horizontal flip.jpg", horizontal_img )
cv2.imwrite( "Vertical flip.jpg", vertical_img )
subimg = cv2.subtract(horizontal_img,vertical_img)
cv2.imwrite("Subtracted image.jpg",subimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
