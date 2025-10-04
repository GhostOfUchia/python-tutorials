import numpy as np

# Dimensions in Arrays
# A dimension in arrays is one level of array depth (nested arrays).
# nested array: are arrays that have arrays as their elements.

o_D_arr = np.array(21)  # o-D array

# 1-D Arrays
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
# These are the most common and basic arrays.
# - You access items by their index: one_D_arr[0] gives 1.
one_D_arr = np.array([1,2,3,4])  # one dimension array

# 2-D Arrays
# A 2D array is like a grid or a table — rows and columns.
two_D_array = np.array([[1,2,3],[1,2,3]])  



three_D_array = np.array([[[1,2,3],[4,5,6]]]) # three dimension array

arr = np.array([1,2,3,4,5],ndmin = 2)

print(arr)
print(three_D_array.ndim)
print(three_D_array)