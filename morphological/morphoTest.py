# -*- coding: utf-8 -*-

import numpy as np
import cv2 
import morphologicalMethods



img =cv2.imread('coins.jpg')
img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#img=morphologicalMethods.erosion(img)
#img=morphologicalMethods.dilatacion(img)
#img=morphologicalMethods.cierre(img)
#img=morphologicalMethods.apertura(img)
img=morphologicalMethods.gradient(img)



cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()