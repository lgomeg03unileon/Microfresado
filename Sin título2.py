# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:09:00 2019

@author: luis_
"""

import numpy as np
from scipy import ndimage


def flood_fill(test_array, four_way=False):


""""""


input_array = np.copy(test_array)




# Set h_max to a value larger than the array maximum to ensure
#   that the while loop will terminate
h_max = np.max(input_array * 2.0)



# Build mask of cells with data not on the edge of the image
# Use 3x3 square structuring element

# Build Structuring element only using NumPy module
# Structuring element could also be built using SciPy ndimage module
#   el = ndimage.generate_binary_structure(2,2).astype(np.int)
data_mask = np.isfinite(input_array)
inside_mask = ndimage.binary_erosion(
    data_mask, 
    structure=np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]).astype(np.bool))
edge_mask = (data_mask & ~inside_mask)
 
# Initialize output array as max value test_array except edges
output_array = np.copy(input_array)
output_array[inside_mask] = h_max
 
# Array for storing previous iteration
output_old_array = np.copy(input_array)
output_old_array.fill(0)   
 
# Cross structuring element
if four_way:
    el = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]).astype(np.bool)
    # el = ndimage.generate_binary_structure(2, 1).astype(np.int)
else:
    el = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]).astype(np.bool)
    # el = ndimage.generate_binary_structure(2, 2).astype(np.int)
 
# Iterate until marker array doesn't change
while not np.array_equal(output_old_array, output_array):
    output_old_array = np.copy(output_array)
    output_array = np.maximum(
        input_array,
        ndimage.grey_erosion(output_array, size=(3, 3), footprint=el))
return output_array