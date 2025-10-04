import numpy as np

# what is array indexing 
# array indexing is the same as accessing an array elements
# you can acess an array elements by referring to its index number
# index number start with 0,1,2,3,4

arr = np.array([1,2,3,4])

print(arr[1])  # it can print 2
print(arr[2]+arr[1])    # it can print 5

# accessing multi dimension array elements
#To access elements from 2-D arrays we can use comma separated integers 
# representing the dimension and the index of the element.
#Think of 2-D arrays like a table with rows and columns, 
# where the dimension represents the row and the index represents the column.

arr2 = np.array([[[1,2,3],[4,5,6]]])

print(arr2[0][0][1])

# nagative indexing
# Use negative indexing to access an array from the end.
arr3 = np.array([[1,2,3],[4,5,6]])

print(arr3[1,-2])

arr4 = np.array([1,2,3,4,5])
print(arr4[-3])