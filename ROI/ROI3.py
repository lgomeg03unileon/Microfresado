# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:01:08 2020

@author: luis_
"""

import cv2
import numpy as np
import math


"""
De entrada una imagen binaria, con area o contorno

"""

def pixelEqual(A,B):
    
    a=np.array(A)
    b=np.array(B)
    return(all(np.equal(a,b)))
    
def inclinacionRecta(p1, p2):
    
    if((p2[0]-p1[0])==0):
        return 90
    
    m=(p2[1]-p1[1])/(p2[0]-p1[0])
    
    
    return (-1)*math.degrees(math.atan(m))

"""
Busca un pixel no 0 desde la izquieda de la imagen y devuelve el punto
A es la posicion del pixel inicial
d distancia en pixeles
"""

def findPixelFromLeft(img, A, d):
    
    aux=A-d
    pixel=img[0][A]
    y=0
    print(aux)
    print(pixel)
    
    
    
    while pixel==0 and aux[1]<=0 and aux[0]>=img.shape[0]:
        y=y+1
        if img[y][aux[1]]!=0:
            return [y, aux[1]]
    return False    
    
    
#TODO: crear una imagen del tamaño de la original, tomar varios puntos del borde, crea
#   un area ROI
    def roi3(img):
        return False
    