"""
Reshaping means changing the shape of an array.

The shape of an array is the number of elements in each dimension.

By reshaping we can add or remove dimensions or change number of elements in each dimension.
"""
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

newArr = arr.reshape(4,2)
# print(newArr)  [[1 2] [3 4] [5 6][7 8]]

newArr2 = arr.reshape(2,2,2)
# print(newArr2)  [[[1 2] [3 4]] [[5 6] [7 8]]]

# newArr3 = arr.reshape(3,3)
# it will raise a error  :- ValueError: cannot reshape array of size 8 into shape (3,3)

newArr4 = arr.reshape(2,4)
# print(newArr4.base) it will return view

#  If you don’t know one dimension, put -1 and NumPy will figure it out.

newArr5 = arr.reshape(2,-1)
# Note: We can not pass -1 to more than one dimension.
# print(newArr5)

# Flattening array means converting a multidimensional array into a 1D array.

# We can use reshape(-1) to do this.

arr1 = np.array([[1,2,3],[4,5,6]])
# print(arr1.reshape(-1)) [1 2 3 4 5 6]

"""
 Note: There are a lot of functions for changing the shapes of arrays 
 in numpy flatten, ravel and also for rearranging 
 the elements rot90, flip, fliplr, flipud etc. 
These fall under Intermediate to Advanced section of numpy.
"""

