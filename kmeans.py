# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:16:07 2019

@author: luis_
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
import preprocessing

img = cv2.imread('coins.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

Z = gray.reshape((-1,1))


# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K =3
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((gray.shape))


cv2.namedWindow('res2',cv2.WINDOW_NORMAL)
cv2.resizeWindow('res2', 600,600)
cv2.imshow('res2',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()