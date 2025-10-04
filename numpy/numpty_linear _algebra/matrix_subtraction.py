import numpy as np

# Creating two 2x2 matrices
A = np.array([[5, 8], [7, 10]])
B = np.array([[2, 4], [3, 6]])

# Print the matrices
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)


# Subtracting two matrices using the - operator
C = A - B

# Print the result
print("Matrix C (A - B):")
print(C)

# Subtracting two matrices using numpy.subtract() function
D = np.subtract(A, B)

# Print the result
print("Matrix C (A - B using numpy.subtract()):")
print(D)

# Subtract a scalar from the matrix using broadcasting
E = A - 5

# Print the result
print("Matrix A - 5:")
print(E)