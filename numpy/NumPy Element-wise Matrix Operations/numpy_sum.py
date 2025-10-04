import numpy as np
# Define a 1D array
arr = np.array([1, 2, 3, 4, 5])

# Calculate the sum of all elements
total_sum = np.sum(arr)

print("Total sum of the array:", total_sum)

# Define a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Sum along rows (axis=1)
sum_rows = np.sum(arr_2d, axis=1,keepdims = True )

# Sum along columns (axis=0)
sum_columns = np.sum(arr_2d, axis=0,keepdims = True)

print("Sum along rows:", sum_rows)
print("Sum along columns:", sum_columns)

# Define an array of integers
arr_int = np.array([10, 20, 30])

# specifie datatype
result = np.sum(arr_int,dtype = np.float64)
print(result)