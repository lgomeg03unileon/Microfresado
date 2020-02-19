# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 13:57:36 2019

@author: luis_
"""

im_floodfill = thresh.copy()
h, w = thresh.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
cv.floodFill(im_floodfill, mask, (0,0), 255)
im_floodfill_inv = cv.bitwise_not(im_floodfill)
im_out = thresh | im_floodfill_inv