# -*- coding: utf-8 -*-

import cv2, math, statistics
import numpy as np



"""

extrae las posiciondes de los punto de interes detectados:sift[x].pt

toma un area y calcula el numero de puntos en el area
"""

def density_sift(sift, k=3):
    
    
    Data=[]
    
    for x in sift:
       Data.append(x.pt)
       
     
        
    Z=np.float32(Data)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
   
    ret,label,center=cv2.kmeans(Z,k,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    
    medias=[]
    c=0
    density=[]
    for a in center:
        distances=[]
        points=Z[label.ravel()==c]
        nPointsInarea=0
        for b in points:
            distances.append(math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2))
        media=statistics.mean(distances)
        medias.append(media)                        #Me sobra?
        
        for b in points:                                        #Se puede optimizar el bucle, como me lo salto?
           d= math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
           if d<= media:
               nPointsInarea+=1
       
        density.append(nPointsInarea/(math.pi*media**2))
        c+=1       
        
    
    #A = Z[label.ravel()==0]         #puntos con etiqueta 0
    
    
    
    
    
    return density