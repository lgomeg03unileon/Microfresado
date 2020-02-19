# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 18:18:51 2019

@author: luis_
"""

import numpy as np
import cv2 as cv

def fillHoles(img):
    im_floodfill = img.copy()
    h, w = img.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    cv.floodFill(im_floodfill, mask, (0,0), 255)
    im_floodfill_inv = cv.bitwise_not(im_floodfill)
    im_out = img | im_floodfill_inv
    
    return im_out

#TODO
def deleteFreaserInfo(img):
    
    
    return img