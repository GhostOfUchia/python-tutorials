import numpy as np

arr1 = np.array([1,2,3])

arr2 = np.array([4,5,6])

arr = np.array([7,8,9])

# rst = np.concatenate((arr1,arr2,arr))

# print(rst)

arr3 = np.array([[1,2,3],[4,5,6]])

arr4 = np.array([[1,2,3],[4,5,6]])

rst1 = np.concatenate((arr3,arr4),axis = 1)

# print(rst1)

"""
Joining Arrays Using Stack Functions

Stacking is same as concatenation,

the only difference is that stacking is done along a new axis.

We can concatenate two 1-D arrays along the second axis

which would result in putting them one over the other, ie. stacking.

We pass a sequence of arrays that we want to join to 

the stack() method along with the axis. 

If axis is not explicitly passed it is taken as 0.
"""

arr6 = np.array([1, 2, 3])

arr7 = np.array([4, 5, 6])

# arr = np.stack((arr6, arr7),axis = 1)
# NumPy provides a helper function: hstack() to stack along rows.

# arr = np.hstack((arr1, arr2))
# NumPy provides a helper function: vstack()  to stack along columns.

# arr = np.vstack((arr1, arr2))
# NumPy provides a helper function: 
# dstack() to stack along height, which is the same as depth.

print(arr)