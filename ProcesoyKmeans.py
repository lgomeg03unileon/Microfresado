# -*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt
import preprocessing
from threshold import thresholdMethods
from morphological import morphologicalMethods
from blur import blurMethods
from ROI3 import roi3
from descriptors import texture

img = cv2.imread('1mm2.tif', 0)
img=preprocessing.deleteFreaserInfo(img)

gray=roi3.roiM1(img)
#cv2.imwrite("ROI3\\roi2.tif",roi3.roiM2(img))
#cv2.imwrite("ROI3\\roi3.tif",roi3.roiM3(img))

dest_and = cv2.bitwise_and(gray, img, mask = None) 

"""
post=texture.LBP_scikit(dest_and,8, 24)
"""

post= texture.SIFT_Opencv(gray)






Z = post.reshape((-1,1))


# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K =2
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((post.shape))


cv2.namedWindow('res2',cv2.WINDOW_NORMAL)
cv2.resizeWindow('res2', 600,600)
cv2.imshow('res2',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()