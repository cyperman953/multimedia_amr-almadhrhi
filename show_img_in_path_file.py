import cv2
import numpy as np
for i in range(1,5,4):
    image =cv2.imread('D:/amr_1/amr_hac/1.jpg')
  
    cv2.imshow('image_hac',image)
    cv2.waitKey(0)
    image1 =cv2.imread('D:/amr_1/amr_hac/2.jpg')
    cv2.imshow('image_hac',image1)
    cv2.waitKey(0)
    image =cv2.imread('D:/amr_1/amr_hac/3.jpg')
  
    cv2.imshow('image_hac',image)
    cv2.waitKey(0)
    image1 =cv2.imread('D:/amr_1/amr_hac/4.jpg')
    cv2.imshow('image_hac',image1)
    cv2.waitKey(0)
    image1 =cv2.imread('D:/amr_1/amr_hac/5.jpg')
    cv2.imshow('image_hac',image1)
    cv2.waitKey(0)
cv2.destroyAllWindows()
    
