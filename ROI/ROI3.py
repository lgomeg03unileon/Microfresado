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
    
    deg =math.degrees(math.atan(m))
    
    if deg<0:
        return 90+deg
    
    return math.degrees(math.atan(m))-90





"""
Busca el primer pixel negro desde la izquieda de la imagen y devuelve el punto
A es la posicion vertical inicial 
d distancia vertical en pixeles desde la posicion inicial

(la que se mueve es la segunda coordenada)
"""
def findPixelFromLeft(img, A, d):
    
    aux=A-d
    y=0
    
    
    print(aux)
    while aux>=0 and aux<=img.shape[0] and y<img.shape[1]-1:
        
        y=y+1
        if img[aux][y]!=0:
            return [aux, y]
        
    return [aux, y]   
    





def adaptarDistancia(p1, p2, d):
    
    deg=abs(inclinacionRecta(p1, p2))
    
    if deg<45:
        return d*(-1)*(90-deg)/90
    return d*(deg/90)

    
#TODO: crear una imagen del tamaño de la original, tomar varios puntos del borde, crea
#   un area ROI
""" 
d distancia base para calcular los puntos
"""


def roi3(img,d):
    firstPixel=findPixelFromLeft(img, img.shape[0]-1,0)
    auxPixel1=findPixelFromLeft(img, img.shape[0]-1,d)
    pixelList=[firstPixel,auxPixel1]
        
         
        
    while pixelList[pixelList.count][0]!=img.shape[1]-1:
            auxPixel1
        
    return img
    