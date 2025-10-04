import numpy as np

"""
Matrix Multiplication (*): This performs element-wise multiplication, 
which is not the same as matrix multiplication. 
It multiplies corresponding elements of the two matrices.

Matrix Multiplication (@): This performs true matrix multiplication, 
following the linear algebra rules. It multiplies the rows of 
the first matrix by the columns of the second matrix.

Matrix Multiplication (np.dot()): The np.dot() function computes 
the dot product of the two matrices, which in the case of 2D arrays, 
equals matrix multiplication.

Matrix Multiplication (np.matmul()): This function works similarly to np.dot() 
but is specifically designed for matrix multiplication.
"""

# Define two matrices
matrix_1 = np.array([[1, 2], [3, 4]])
matrix_2 = np.array([[5, 6], [7, 8]])

# Matrix multiplication using *
result_1 = matrix_1 * matrix_2

# Matrix multiplication using @
result_2 = matrix_1 @ matrix_2

# Matrix multiplication using np.dot()
result_3 = np.dot(matrix_1, matrix_2)

# Matrix multiplication using np.matmul()
result_4 = np.matmul(matrix_1, matrix_2)

matrix_1 = np.array([[1, 2, 3], [4, 5, 6]])
matrix_2 = np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])

result = np.matmul(matrix_1, matrix_2)
print(result)