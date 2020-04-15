# -*- coding: utf-8 -*-
import numpy as np
import cv2
from ROI3 import roi3
from descriptors import texture
from density import density

img = cv2.imread('img-33.tif')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
       
roi=roi3.roiM1(gray)
        
dest_and = cv2.bitwise_and(roi, gray, mask = None)


sift = texture.SIFT_Opencv(dest_and)

den=density.density_sift(sift, k=5)

print(den)

