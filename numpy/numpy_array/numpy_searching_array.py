"""
✨ So in short:

np.where() → find indexes by condition

np.isin() → check membership

np.nonzero() → find non-zeros

np.argmax() / np.argmin() → find first max/min index
 """


import  numpy as np

arr = np.array([1,2,3,3,4,5,5,7,3,5])

x = np.where(arr == 3) 

# The example above will return a tuple: (array([2,3,7],)
# Which means that the value 3 is present at index 2, 3, and 7.

y = np.where(arr%3 == 2) 

arr2 = np.array([3, 6, 7, 8, 9,5])

z = np.searchsorted(arr2, 8,side = 'right')



arr3 = np.array([10, 20, 30, 40, 50])

# Find where elements are greater than 25
indices = np.where(arr3 > 25)
# print(indices)       # (array([2, 3, 4]),)
# print(arr[indices])  # [30 40 50]


# Check if an element exists – np.isin()
arr = np.array([1, 2, 3, 4, 5])

# print(np.isin(arr, [2, 3,5]))   # [ False true true False  True]


# 👉 Tells whether each element is inside the given list.

# Find first occurrence – np.argmax() with condition
arr = np.array([0, 0, 1, 0, 1,3,3])

first_one = np.argmax(arr == 1)
# print(first_one)  # 2

              #Find non-zero elements – np.nonzero()
arr = np.array([0, 7, 0, 8, 0,4])

# print(np.nonzero(arr))  # (array([1, 3]),)

t = np.searchsorted(arr2, [2, 4, 6])

print(x)
