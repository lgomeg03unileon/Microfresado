# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:54:14 2020

@author: luis_
"""

import cv2
img = cv2.imread("coins.jpg")
crop_img = img[200:250, 200:250]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)