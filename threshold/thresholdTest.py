# -*- coding: utf-8 -*-

import numpy as np
import cv2
import thresholdMethods

img = cv2.imread('img-33.tif', 0)

#img=thresholdMethods.simpleThreshold(img,159,255,cv2.THRESH_BINARY)
#img=thresholdMethods.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
img=thresholdMethods.otsuThreshold(img,0,255,cv2.THRESH_BINARY)


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()