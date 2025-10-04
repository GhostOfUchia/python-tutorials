

import numpy as np
# define a square matrix
arr = np.array([[1,2],[3,4]])

# calculate inversion
arr_inv = np.linalg.inv(arr)
print(arr_inv)

# Verifying the inverse
ver_anv = np.dot(arr,arr_inv)
print(ver_anv)

# Coefficient matrix
A = np.array([[1, 2], [3, 4]])

# Constant vector
B = np.array([[5], [6]])

# Compute the inverse of A
A_inv = np.linalg.inv(A)

# Solve for X
X = np.dot(A_inv, B)
print(X)


def calculate_inverse(matrix):
      try:
       return np.linalg.inv(matrix)
      except np.linalg.LinAlgError:
       return "Matrix is not invertible."
      
matrix = np.array([[1,2],[2,4]])   
result = calculate_inverse(matrix)
print(result)   