# -*- coding: utf-8 -*-


import numpy as np
import cv2 


def erosion(img,kernel=np.ones((5,5),np.uint8),iters = 1):
    
    return  cv2.erode(img,kernel,iterations=iters)

def dilatacion(img,kernel=np.ones((5,5),np.uint8),iters = 1):
    return cv2.dilate(img,kernel,iterations =iters)

def apertura(img,kernel=np.ones((5,5),np.uint8)):
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

def cierre(img,kernel=np.ones((5,5),np.uint8)):
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    
def gradient(img,kernel=np.ones((5,5))):
    return cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)