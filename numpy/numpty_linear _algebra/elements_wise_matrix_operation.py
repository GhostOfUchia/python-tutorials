import numpy as np

# Define two matrices
matrix_1 = np.array([[1, 2], [3, 4]])
matrix_2 = np.array([[5, 6], [7, 8]])

# Element-wise addition
result = matrix_1 + matrix_2
print(result)

# Element-wise subtraction
result1 = matrix_1 - matrix_2
print(result1)

# Element-wise multiplication
result3 = matrix_1 * matrix_2
print(result3)

# Element-wise division
result4 = matrix_1 / matrix_2
print(result4)

# Define a matrix and a scalar

scalar = 2

# Element-wise addition with scalar
result_add = matrix_1 + scalar
print(result_add)

# Element-wise multiplication with scalar
result_mul = matrix_1 * scalar
print(result_mul)

# Define two matrices
array_1 = np.array([5, 6])

# Broadcasting example
result6 = matrix_1 + array_1
print(result6)