# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:52:31 2020

@author: luis_
"""

import numpy as np
import cv2
import blurMethods


img = cv2.imread('coins.jpg')

#img= blurMethods.gaussian(img, kernel=(15,15))
#img= blurMethods.median(img, aperture=3)
img=blurMethods.blur2dfilter(img)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()