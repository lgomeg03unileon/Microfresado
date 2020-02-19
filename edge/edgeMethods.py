# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 13:54:34 2020

@author: luis_
"""

import cv2

def canny(img):
    return cv2.Canny(img, 100,300)