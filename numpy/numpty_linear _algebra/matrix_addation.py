import numpy as np

# Creating two 2x2 matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Print the matrices
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)



# Adding two matrices using the + operator
C = A + B
# Print the result
print("Matrix C (A + B):")
print(C)


# Adding two matrices using numpy.add() functio
D = np.add(A, B)
# Print the result
print("Matrix C (A + B using numpy.add()):")
print(D)

# Add a scalar to the matrix using broadcasting
E = A + 10

# Print the result
print("Matrix A + 10:")
print(E)