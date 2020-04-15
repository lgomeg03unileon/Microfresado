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




"""


¿ HAY ALGUNA FORMA DE UTILIZAR SIFT CON KMEANS PARA CONOCER EL ESTADO DE LA HERRAMIENTA?



"""
img = cv2.imread('img-33.tif')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
       
roi=roi3.roiM1(gray)
        
dest_and = cv2.bitwise_and(roi, gray, mask = None)


sift = texture.SIFT_Opencv(dest_and)
#kp = sift.detect(gray,None)
img=cv2.drawKeypoints(gray,sift,img)


Z = sift.reshape((-1,1))        #TODO


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


