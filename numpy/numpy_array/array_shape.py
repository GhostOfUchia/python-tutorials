"""
In NumPy, every array has a shape that tells you 
its dimensions (how many rows, columns, etc.).

👉 The shape is stored in the .shape attribute.
It returns a tuple of integers.


"""

import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])

# print(arr.shape) 
# The example above returns (2, 4), which means that the array has 2 dimensions, 
# where the first dimension has 2 elements and the second has 4.

arr1 = np.array([1,2,3,4,5])
# print(arr1.shape)  (5,) This means the array has 5 elements in one dimension.

arr3 = np.array([1,2,3,4],ndmin = 5)

print(arr3.shape)
 

 