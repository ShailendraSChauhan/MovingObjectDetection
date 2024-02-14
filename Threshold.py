import cv2

img = cv2.imread("Digital.jpg")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshImg = cv2.threshold(grayImg, 150, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite("Threshold.jpg", threshImg)
cv2.imshow("Threshold Image", threshImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
