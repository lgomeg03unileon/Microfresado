# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 22:59:16 2020

@author: luis_
"""

import numpy as np
import cv2

#Normaliced Average blurring
def average(img, kernel=(3,3)):
    return cv2.blur(img, kernel)

#Not Normaliced Average blurring
#Pierde las propiedades de la imagen
def averageNotNormaliced(img, depth=0,kernel=(3,3), border=cv2.BORDER_DEFAULT):
    return cv2.boxFilter(src=img, ddepth=0, ksize=kernel, normalize=False,borderType=border)
    
#Gaussian filter blur
#Kernel debe ser impar
def gaussian(img, kernel=(5,5), standardDeviation=0):
    return cv2.GaussianBlur(img, kernel,standardDeviation)

#Media filter blur
def median(img, aperture=3):
    return cv2.medianBlur(img, aperture)


def bilateral(img, diameter=9,sigmacolor=75,sigmaspace=75):
    return cv2.bilateralFilter(img,diameter,sigmacolor,sigmaspace)


def blur2dfilter(img, kernel=np.ones((5,5),np.float32)/25):
    return cv2.filter2D(img,-1,kernel)