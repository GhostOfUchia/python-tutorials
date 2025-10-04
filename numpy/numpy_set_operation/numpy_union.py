"""
In NumPy, the term "union" refers to the operation that combines 
the elements of two or more 
arrays, removing any duplicate values.

It is commonly used when you want to merge multiple datasets or arrays, 
ensuring that each element appears only once in the final result.

NumPy provides the numpy.union1d() function to easily find the union of
 two 1-dimensional arrays.
"""
import numpy as np
from functools import reduce

# Define two 1-d array
arr1 = np.array([1,2,3,3,4,5])
arr2 = np.array([6,7,8,9,9,3])

# find union of two array
arr3 = np.union1d(arr1,arr2)
# print(arr3)

# Define arrays with different data types
array5 = np.array([1, 2, 3, 4.5])
array6 = np.array([4.5, 5, 6, 7])

# find union of two different datatype arrays
array7 = np.union1d(array5,array6)
print(array7)

#  Find the union of all arrays

result = reduce(np.union1d,[arr1,arr2,arr3])
print(result)

# Define arrays with strings
strarray1 = np.array(['apple', 'banana', 'cherry'])
strarray2 = np.array(['banana', 'cherry', 'date','grapes'])

# Find the union of the string arrays
union = np.union1d(strarray1, strarray2)

print("Union of string arrays:", union)

# Define arrays with unique elements
array9 = np.array([1, 2, 3, 4, 5])
array10 = np.array([6, 7, 8, 9, 10])

# Find union assuming unique elements
union = np.union1d(array9, array10)

print("Union of unique arrays:", union)