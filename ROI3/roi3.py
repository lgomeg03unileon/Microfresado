# -*- coding: utf-8 -*-

import os,sys,inspect, cv2
import numpy as np
import preprocessing
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from threshold import thresholdMethods
from morphological import morphologicalMethods
from blur import blurMethods

def roiM1(img):
    blur = blurMethods.gaussian(img, standardDeviation=21)
    otsu = thresholdMethods.otsuThreshold(blur, 0, 255, cv2.THRESH_BINARY)

   
    imagem=preprocessing.fillHoles(otsu)
    imagem = cv2.bitwise_not(imagem)
    dilation = morphologicalMethods.dilatacion(imagem, iters=40)
    
    
    
    dest_xor = cv2.bitwise_xor(imagem, dilation, mask = None) 
    #roi=cv2.bitwise_not(dest_xor)
    
   # dest_and = cv2.bitwise_and(roi, img, mask = None) 
    return dest_xor



def roiM2(img,d=300):
    blur = blurMethods.gaussian(img, standardDeviation=21)
    otsu = thresholdMethods.otsuThreshold(blur, 0, 255, cv2.THRESH_BINARY)
    
    
    edges = morphologicalMethods.dilatacion(otsu, iters=3)
    edges=cv2.Canny(edges, 0,255)
    
    leftP=img.shape[0]
    
    
    
    
    linesP = cv2.HoughLinesP(edges,1, np.pi/360, 50, None, 50, 150)
    if linesP is not None:
            for i in range(0, len(linesP)):
                l = linesP[i][0]
                if leftP>l[0]:
                    leftP=l[0]
                if leftP>l[2]:
                    leftP=l[2]
               
                
                #cv2.line(img, (l[0], l[1]), (l[2], l[3]), (255,255,255), 3, cv2.LINE_AA)
    black=np.zeros((img.shape[0], img.shape[1]),np.uint8)

    cv2.rectangle(black, (leftP, img.shape[0]), (leftP+d, 0), (255,255,255), -1)
    
    
    dest_and = cv2.bitwise_and(otsu, black, mask = None) 
    return dest_and


"""metodo 1 y 2 a la vez"""
def roiM3(img,d=300):
    blur = blurMethods.gaussian(img, standardDeviation=21)
    otsu = thresholdMethods.otsuThreshold(blur, 0, 255, cv2.THRESH_BINARY)
    
    
    edges = morphologicalMethods.dilatacion(otsu, iters=3)
    edges=cv2.Canny(edges, 0,255)
    
    leftP=img.shape[0]
    
    
    
    
    linesP = cv2.HoughLinesP(edges,1, np.pi/360, 50, None, 50, 150)
    if linesP is not None:
            for i in range(0, len(linesP)):
                l = linesP[i][0]
                if leftP>l[0]:
                    leftP=l[0]
                if leftP>l[2]:
                    leftP=l[2]
               
                
                #cv2.line(img, (l[0], l[1]), (l[2], l[3]), (255,255,255), 3, cv2.LINE_AA)
    black=np.zeros((img.shape[0], img.shape[1]),np.uint8)

    cv2.rectangle(black, (leftP, img.shape[0]), (leftP+d, 0), (255,255,255), -1)
    
    
    dest_and = cv2.bitwise_and(roiM1(img), black, mask = None) 
    return dest_and


def findPixelFromLeft(img, A, d):
    
    aux=A-d
    y=0
    
    while aux>=0 and aux<=img.shape[0] and y<img.shape[1]-1:
        
        y=y+1
        if img[aux][y]!=0:
            return [aux, y]
        
    return [aux, y]   