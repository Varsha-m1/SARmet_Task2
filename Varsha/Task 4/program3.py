import cv2
img = cv2.imread("720x1280.jpg")
img1 = cv2.resize(img, (240,1280))
cv2.imwrite("Cropped image.jpg",img1)
laplacian = cv2.Laplacian(img1,cv2.CV_64F)
cv2.imwrite('Laplacian.jpg',laplacian)
