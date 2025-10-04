import numpy as np

# Define a 2x2 matrix
A = np.array([[1, 2], [3, 4]])

# Compute the determinant of the matrix
det_A = np.linalg.det(A)
print(det_A)

# Define a 3x3 matrix
B = np.array([[6, 1, 1], 
              [4, -2, 5], 
              [2, 8, 7]])

# Compute the determinant of the matrix
det_B = np.linalg.det(B)
print(det_B)

# Coefficient matrix
A = np.array([[2, 1], [5, 7]])

# Constant vector
B = np.array([11, 13])

# Solve for X using Cramer's Rule
det_A = np.linalg.det(A)
A1 = np.array([[11, 1], [13, 7]])
A2 = np.array([[2, 11], [5, 13]])

X1 = np.linalg.det(A1) / det_A
X2 = np.linalg.det(A2) / det_A

X = np.array([X1, X2])
print(X)

def calculate_determinant(matrix):
   try:
      return np.linalg.det(matrix)
   except np.linalg.LinAlgError:
      return "Matrix is singular and has no determinant."

# Singular matrix
C = np.array([[1, 2], [2, 3]])

# Attempt to compute the determinant
result = calculate_determinant(C)
print(result)