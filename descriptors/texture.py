# -*- coding: utf-8 -*-

import mahotas
from skimage import feature
from skimage.feature import greycomatrix, greycoprops
from skimage import data
from skimage.util import img_as_float
from skimage.filters import gabor_kernel
import numpy as np
import cv2

"""
https://gogul.dev/software/texture-recognition
"""

def haralick_features_mahotas(image):
        # calculate haralick texture features for 4 types of adjacency
        textures = mahotas.features.haralick(image)

        # take the mean of it and return it
        ht_mean = textures.mean(axis=0)
        return ht_mean
    
    
    


"""
https://scikit-image.org/docs/dev/auto_examples/features_detection/plot_glcm.html
"""

def GLCM_features_scikit(image):
    xs = []
    ys = []
    glcm = greycomatrix(image, distances=[5], angles=[0], levels=256,
                        symmetric=True, normed=True)
    xs.append(greycoprops(glcm, 'dissimilarity')[0, 0])
    ys.append(greycoprops(glcm, 'correlation')[0, 0])
    
    return [xs,ys]


def SIFT_Opencv(img):
    
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(img,None)
    
    return kp


"""
https://www.pyimagesearch.com/2015/12/07/local-binary-patterns-with-python-opencv/
"""

def LBP_scikit(img,r, p, eps=1e-7):
    lbp = feature.local_binary_pattern(img, p, r, method="uniform")
    (hist, _) = np.histogram(lbp.ravel(),
			bins=np.arange(0, p + 3),
			range=(0, p + 2))
    # normalize the histogram
    hist = hist.astype("float")
    hist /= (hist.sum() + eps)
    return lbp


"""
    ksize	Size of the filter returned.
    sigma	Standard deviation of the gaussian envelope.
    theta	Orientation of the normal to the parallel stripes of a Gabor function.
    lambd	Wavelength of the sinusoidal factor.
    gamma	Spatial aspect ratio.
 
"""
def gabor(img,size, sigm, thet, lam, gam, phas):
     kernel =cv2.getGaborKernel(ksize=size,sigma=sigm, theta=thet, lambd=lam, gamma=gam, psi=phas)
     #kernel = cv2.getGaborKernel((21, 21), 8.0, np.pi/4, 10.0, 0.5, 0, ktype=cv2.CV_32F)
     filtered_img = cv2.filter2D(img, cv2.CV_8UC3, kernel)

     return filtered_img
    
