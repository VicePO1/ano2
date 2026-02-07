import cv2

img=cv2.imread('jeff.jpg',0)
img=cv2.resize(img,(0,0),fx=1.3,fy=1.3)
img=cv2.rotate(img,cv2.ROTATE_180)
cv2.imshow('Jeff',img)
cv2.waitKey(0)

cv2.destroyAllWindows()