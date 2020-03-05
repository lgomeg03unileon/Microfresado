# -*- coding: utf-8 -*-

import numpy as np
import cv2
from threshold import thresholdMethods
from morphological import morphologicalMethods
from blur import blurMethods
from ROI3 import roi3

img = cv2.imread('img-33.tif', 0)

cv2.imwrite("ROI3\\roi1.tif",roi3.roiM1(img))
cv2.imwrite("ROI3\\roi2.tif",roi3.roiM2(img))
cv2.imwrite("ROI3\\roi3.tif",roi3.roiM3(img))



cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.resizeWindow('img', 600,600)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()