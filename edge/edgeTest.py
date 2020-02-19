# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 11:38:25 2020

@author: luis_
"""


import numpy as np
import cv2
import edgeMethods


img = cv2.imread('img-33.tif')
img = edgeMethods.canny(img)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
