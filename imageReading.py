# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 17:29:55 2020

@author: luis_
"""

import cv2
import os
import sys

import preprocessing

from ROI3 import roi3

currentPath=os.getcwd()
subfolders=["0_0m", "0_2m", "0_4m", "0_6m","0_8m", "1_0m", "2_0m", "3_0m","4_0m"]
for y in subfolders:
    subpath=currentPath+"\\dataset\\tipo3\\"+y+"\\400\\"
    for x in os.listdir(subpath):  #currentPath+"\\dataset\\"+y+"\\400\\"):
        img = cv2.imread(subpath+x, 0)
        img=preprocessing.deleteFreaserInfo(img)
        
        roi=roi3.roiM1(img)
        
        dest_and = cv2.bitwise_and(roi, img, mask = None)
        
        cv2.namedWindow('img',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('img', 600,600)
        cv2.imshow('img',dest_and)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
