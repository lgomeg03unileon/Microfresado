# -*- coding: utf-8 -*-

import numpy as np
import cv2
import pywt
import pywt.data
import matplotlib.pyplot as plt
from threshold import thresholdMethods
from morphological import morphologicalMethods
from blur import blurMethods
from ROI3 import roi3
from descriptors import texture

img = cv2.imread('damage.tif')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
       
roi=roi3.roiM2(gray)
        
dest_and = cv2.bitwise_and(roi, gray, mask = None)

"""
HARALICK

dest_and = cv2.bitwise_and(roi3.roiM1(gray), img, mask = None) 
texture.haralick_features(dest_and)
"""
"""
SIFT
"""

sift = texture.SIFT_Opencv(dest_and)
#kp = sift.detect(gray,None)
img=cv2.drawKeypoints(img,sift,img)
print(sift[1].pt)

"""
LBP
lbp=texture.LBP_scikit(gray,8, 24)

"""

"""
Gabor


kernel=texture.gabor(dest_and, (21, 21), 9.0, 2*np.pi/3, 10.0, 0.9,0)

#kernel=texture.gabor(dest_and, (21, 21), 9.0, np.pi, 10.0, 0.9,0)

"""
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.resizeWindow('img', 600,600)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
titles = ['Approximation', ' Horizontal detail',
          'Vertical detail', 'Diagonal detail']

coeffs2 = pywt.dwt2(dest_and, 'bior1.3')
LL, (LH, HL, HH) = coeffs2

fig = plt.figure(figsize=(12, 3))
for i, a in enumerate([LL, LH, HL, HH]):
    ax = fig.add_subplot(1, 4, i + 1)
    ax.imshow(a, interpolation='nearest', cmap=plt.cm.gray)
    ax.set_title(titles[i], fontsize=10)
    ax.set_xticks([])
    ax.set_yticks([])

fig.tight_layout()
plt.savefig('dest.jpg', format='jpg', dpi=700)
"""