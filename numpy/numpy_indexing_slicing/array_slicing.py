"""
Slicing in python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1 """

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

print(arr[0:5])   # [1 2 3 4 5]
#  The result includes the start index, but excludes the end index.

print(arr[4:])  # [5 6 7 8]

print(arr[:4])  # [1 2 3 4]

# Use the minus operator to refer to an index from the end:
print(arr[-3:-1])  # [6 7]

# Use the step value to determine the step of the slicing:

print(arr[0:7:2])  # [1 3 5 7]

# Return every other element from the entire array:

print(arr[::2])  # [1 3 5 7]

arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])

# print(arr2[1,1:4])  # [7 8 9]

# print(arr2[0:3,3])  # [ 4  9 14]

print(arr2[0:3,1:4])