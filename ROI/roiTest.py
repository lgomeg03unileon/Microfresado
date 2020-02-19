# -*- coding: utf-8 -*-

import cv2
import numpy as np
import ROI3

def pixelEqual(A,B):
    
    a=np.array(A)
    b=np.array(B)
    return(all(np.equal(a,b)))

def pintaArriba(img, x,y):

    aux=0
    while  aux<img.shape[1]-1:
        img[img.shape[1]-aux,0]=100
        aux=aux+1
        

img = cv2.imread('coins.jpg', cv2.IMREAD_COLOR)
img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#img = cv2.imread('img-33.tif', cv2.IMREAD_COLOR)
#pixel=img[img.size[1],img.size[2]]
#print (img.shape[:2])

img=cv2.GaussianBlur(img,(5,5),0)
ret, img = cv2.threshold(img,0,255,cv2.THRESH_BINARY)
"""
aux=img.shape[0]
aux2=0

while aux2<img.shape[1]:
    if(pixelEqual(img[1023, aux2],[255,255,255])):
        pintaArriba(img, 1023,aux2)
        break
        
    else:
        aux2=aux2+1
"""
aux=img.shape[0]-1
"""
while  aux>50:
    img[aux,200]=100
    aux=aux-1
"""
cv2.line(img,(0, 20), (0, 10),(0, 255, 0))

print(ROI3.inclinacionRecta((0, 50), (0, 20)))


cv2.namedWindow('res2',cv2.WINDOW_NORMAL)
cv2.resizeWindow('res2', 600,600)
cv2.imshow('res2',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#print(img[img.shape[0]-1,img.shape[1]-1])

#print(img[img.shape[0]-1,0])

#print(img[0, img.shape[2]-1])
#print(img[0, 0])
