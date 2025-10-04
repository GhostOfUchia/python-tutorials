import numpy as np

# Define two vectors
vector_1 = np.array([1, 2, 3])
vector_2 = np.array([4, 5, 6])
# how dot product ic calculate 
# (1 * 4) + (2 * 5) + (3 * 6) = 32 
result = np.dot(vector_1,vector_2)
print(result)

# Define two matrices
matrix_1 = np.array([[1, 2], 
                     [3, 4]])
matrix_2 = np.array([[5, 6], 
                     [7, 8]])

# Compute dot product
matrix_product = np.dot(matrix_1, matrix_2)
#[[1*5 + 2*7, 1*6 + 2*8],
#[3*5 + 4*7, 3*6 + 4*8]]
print(matrix_product)

# Define two 3-dimensional arrays
array_1 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
array_2 = np.array([[[1, 0], [0, 1]], [[1, 1], [1, 0]]])

# Compute dot product
array_product = np.dot(array_1, array_2)
print(array_product)

# Using @ operator for matrix multiplication
matrix_product1 = matrix_1 @ matrix_2
print(matrix_product1)

# Define input vector (features)
input_vector = np.array([0.5, 1.5, -1.0])

# Define weight vector (weights)
weights = np.array([2.0, -1.0, 0.5])

# Compute the weighted sum (dot product)
output = np.dot(input_vector, weights)
print(output)