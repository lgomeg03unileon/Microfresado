# -*- coding: utf-8 -*-

import numpy as np
import cv2

img = cv2.imread('img-33.tif')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 10
linesP = cv2.HoughLinesP(edges,1, np.pi / 180, 50, None, 100, 10)
if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv2.line(img, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv2.LINE_AA)
cv2.imwrite('houghlines2.jpg',img)

cv2.imshow('img',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()