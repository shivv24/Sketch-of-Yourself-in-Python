import cv2
img=cv2.imread('img.jpg',3)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
inverted=cv2.bitwise_not(gray)
smoothen=cv2.GaussianBlur(inverted,(21,21),sigmaX=0,sigmaY=0)
def dodge(a,b):
    return cv2.divide(a,255-b,scale=256)
final_img=dodge(gray,smoothen)
cv2.imwrite('final.jpg',final_img)
cv2.imshow('Final',final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

