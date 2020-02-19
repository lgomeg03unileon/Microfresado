# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:43:38 2020

@author: luis_
"""

import cv2
import numpy as np
import ROI3


img = cv2.imread('coins.jpg', cv2.IMREAD_COLOR)
img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#img = cv2.imread('img-33.tif', cv2.IMREAD_COLOR)
#pixel=img[img.size[1],img.size[2]]
#print (img.shape[:2])

img=cv2.GaussianBlur(img,(5,5),0)
ret, img = cv2.threshold(img,100,255,cv2.THRESH_BINARY)

print(ROI3.findPixelFromLeft(img, img.shape[1]-1,0))

cv2.namedWindow('res2',cv2.WINDOW_NORMAL)
cv2.resizeWindow('res2', 600,600)
cv2.imshow('res2',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
