import numpy as np

"""
Sorting means putting elements in an ordered sequence.

Ordered sequence is any sequence that has an order corresponding to elements, 

like numeric or alphabetical, ascending or descending.

Summary:

np.sort() → returns sorted array (does not change original)

.sort() → sorts in place

np.argsort() → gives indexes of sorted order

Works with 1D & 2D arrays, along rows/columns
"""

arr = np.array([3, 2, 0, 1])


print(np.sort(arr))
# This method returns a copy of the array, leaving the original array unchanged.
arr.sort()
print(arr)

# sort String array
arr1 = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr1))

# sorting boolean array
arr = np.array([True, False, True])

print(np.sort(arr))

# If you use the sort() method on a 2-D array, both arrays will be sorted:
arr2 = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr2,axis = 0)) # sorting column wise

print(np.sort(arr2,axis = 0)) # sorting row wise

# Get Sorted Indexes with np.argsort()
arr3 = np.array([5, 2, 9, 1, 7])

indexes = np.argsort(arr3)
"""
np.argsort() – Meaning

It gives you the indices that would sort an array.

Instead of giving back the sorted values, 

it tells you where those values are located.
"""

print(indexes)       # [3 1 0 4 2]


print(arr3[indexes])  # [1 2 5 7 9]

 #  Sorting in Descending Order
arr = np.array([5, 2, 9, 1, 7])

descending = np.sort(arr)[::-1]
ascending = np.sort(arr)[::1]
print(descending)  # [9 7 5 2 1]
print(ascending)   # [1,2,5,7,9]