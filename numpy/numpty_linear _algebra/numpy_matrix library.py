import numpy as np

arr = np.array([[1,2],[3,4]])
# converting array in to a matrix with a matrix() function
matrix = np.matrix(arr)
print("With Matrix Function",matrix)


as_matrix = np.asmatrix(arr)
print("With asmatrix() function ",as_matrix)

# Creating a matrix from a string
arr_string = np.matrix('1,2,3;4,6,7;9,2,1')
print("convert matrix string",arr_string)

# Add two matrices
matrix_3 = np.array([[1, 2], [3, 4]])
matrix_4 = np.array([[5, 6], [7, 8]])

result = matrix_3 + matrix_4
# print(result)

# Matrix multiplication
matrix_1 = np.array([[1, 2], [3, 4]])
matrix_2 = np.array([[5, 6], [7, 8]])

# Matrix multiplication using *
matrix_product1 = matrix_1 * matrix_2
# Element-wise (*) → multiply each element with the same position:
print("Matrix Multiplication (*):\n", matrix_product1)

# Matrix multiplication using @
matrix_product2 = matrix_1 @ matrix_2
# Matrix multiplication (@) → row × column rule:
print("Matrix Multiplication (@):\n", matrix_product2)

# Matrix multiplication using np.dot()
matrix_product3 = np.dot(matrix_1, matrix_2)
print("Matrix Multiplication (np.dot()):\n", matrix_product3)

# Matrix multiplication using np.matmul()
matrix_product4 = np.matmul(matrix_1, matrix_2)
print("Matrix Multiplication (np.matmul()):\n", matrix_product4)