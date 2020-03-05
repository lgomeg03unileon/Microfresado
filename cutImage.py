# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:54:14 2020

@author: luis_
"""

import cv2
import preprocessing


img = cv2.imread("1mm.tif")

crop_img =preprocessing.deleteFreaserInfo(img)

cv2.imwrite("cut.tif", crop_img)
cv2.namedWindow('crop_img',cv2.WINDOW_NORMAL)
cv2.resizeWindow('crop_img', 600,600)
cv2.imshow('crop_img',crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()