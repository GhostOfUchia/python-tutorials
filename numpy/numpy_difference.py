"""
In NumPy, the difference operation is used to find elements present in 
one array but not in another. It is commonly used to compare two arrays 
and identify the unique elements in one array that do not exist in the other.

In NumPy, the setdiff1d() function is used to perform this operation.
"""
import numpy as np
from functools import reduce

# Define two arrays
array1 = np.array([1, 2, 3, 4, 5,8,9])
array2 = np.array([3, 4, 5, 6, 7])

# Find the difference between the two arrays
difference = np.setdiff1d(array1, array2)

print("Difference between array1 and array2:", difference)

# Handling Arrays with Duplicate Elements

# Define arrays with duplicate elements
array3 = np.array([1, 2, 2, 3, 4])
array4 = np.array([3, 4, 4, 5, 6])

# Find the difference between the arrays
difference1 = np.setdiff1d(array3, array4)

print("Difference with duplicates removed:", difference1)

# Handling Arrays with Different Data Types
# Define arrays with different data types
array5 = np.array([1, 2, 3, 4.5,5.4])
array6 = np.array([4.5, 5, 6])

# Find the difference between the arrays
difference2 = np.setdiff1d(array5, array6)

print("Difference with different data types:", difference2)

# Difference with Multiple Arrays

# Define multiple arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 4, 5, 6, 7])
arr3 = np.array([5, 6, 7, 8])

# Calculate the difference of all arrays
difference5 = reduce(lambda x, y: np.setdiff1d(x, y), [arr1, arr2, arr3])

print("Difference of multiple arrays:", difference5)

"""
Performance Considerations
The numpy.setdiff1d() function is quite efficient, but performance can 
be a consideration when dealing with large arrays.

If your arrays contain only unique elements, you can use the assume_unique 
parameter to speed up the computation.

Example
By setting theassume_unique parameter to True, NumPy optimizes the 
operation when dealing with arrays that already contain unique elements, 
leading to faster performance as shown in the example below −
"""
# Define arrays with unique elements
a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([3, 4, 5, 6, 7])

# Find the difference assuming unique elements
difference6= np.setdiff1d(a1, a2, assume_unique=True)

print("Difference with unique elements:", difference6)