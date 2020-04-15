# -*- coding: utf-8 -*-




"""Prubas
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt



Data=[[27,30], [41, 47], [27,45], [27,48], [27,50], [33,26], [48,36]]

Z=np.float32(Data)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K =3
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

x,y = zip(*Data)
#plt.scatter(x, y)
#plt.show()  
A = Z[label.ravel()==0]
B = Z[label.ravel()==1]
C = Z[label.ravel()==2]

"""
plt.scatter(A[:,0],A[:,1], c='b')
plt.scatter(B[:,0],B[:,1],c = 'r')
plt.scatter(C[:,0],C[:,1],c = 'g')
plt.scatter(center[:,0],center[:,1],s = 80,c = 'y', marker = 's')
plt.xlabel('Height'),plt.ylabel('Weight')
plt.show()

print(label.ravel())
"""