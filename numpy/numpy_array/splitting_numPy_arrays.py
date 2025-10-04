 #  np.split() → General split by indices

 # np.array_split() → Similar, but allows uneven splits

 # np.hsplit() → Split horizontally (columns)

 # np.vsplit() → Split vertically (rows)

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

newarr1 =  np.split(arr, 2)

# print(newarr)
# print(newarr1)

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

newarr3  = np.hsplit(arr2,3)

newarr4 = np.vsplit(arr2,3) # vsplit only works on arrays of 2 or more dimensions'

print(newarr3)

print(newarr4)