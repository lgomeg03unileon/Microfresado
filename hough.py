# -*- coding: utf-8 -*-


import numpy as np
import cv2
from threshold import thresholdMethods
from morphological import morphologicalMethods

img = cv2.imread('img-33.tif', 0)


edges = thresholdMethods.otsuThreshold(img, 0, 255, cv2.THRESH_BINARY)
edges = morphologicalMethods.dilatacion(edges, iterations=3)
edges=cv2.Canny(edges, 0,255)

linesP = cv2.HoughLinesP(edges,1, np.pi/360, 50, None, 50, 150)
if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv2.line(img, (l[0], l[1]), (l[2], l[3]), (255,255,255), 3, cv2.LINE_AA)
#cv2.imwrite('houghlines2.jpg',img)
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.resizeWindow('img', 600,600)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()