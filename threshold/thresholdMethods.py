# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:23:35 2020

@author: luis_
"""

import numpy as np
import cv2


"""
Tipo puede se:
    -cv2.THRESH_BINARY
    -cv2.THRESH_BINARY_INV
    -cv2.THRESH_TRUNC
    -cv2.THRESH_TOZERO
    -cv2.THRESH_TOZERO_INV
"""
    
def simpleThreshold(img, thresh, maxVal, tipo=cv2.THRESH_BINARY):
    ret,img = cv2.threshold(img,thresh,maxVal,tipo)
    return img




"""
adapt puede ser:
    -cv2.ADAPTIVE_THRESH_MEAN_C
    -cv2.ADAPTIVE_THRESH_GAUSSIAN_C
   
Tipo puede se:
    -cv2.THRESH_BINARY
    -cv2.THRESH_BINARY_INV
    -cv2.THRESH_TRUNC
    -cv2.THRESH_TOZERO
    -cv2.THRESH_TOZERO_INV

"""
def adaptiveThreshold(img, maxVal,adapt,  tipo,tamBloque, constante=2):
    img=cv2.adaptiveThreshold(img, maxVal, adapt, tipo, tamBloque, constante)
    

    return img



"""
Tipo puede se:
    -cv2.THRESH_BINARY
    -cv2.THRESH_BINARY_INV
    -cv2.THRESH_TRUNC
    -cv2.THRESH_TOZERO
    -cv2.THRESH_TOZERO_INV
"""
def otsuThreshold(img, thresh, maxVal, tipo=cv2.THRESH_BINARY):
    ret,img = cv2.threshold(img,thresh,maxVal,tipo+cv2.THRESH_OTSU)
    return img

    
    
    
    
    
    