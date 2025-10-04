import numpy as np

# Define a 3x3 matrix
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Compute the Singular Value Decomposition
U, S, VT = np.linalg.svd(A)

print("Matrix U:\n", U)
print("Singular values:", S)
print("Matrix V^T:\n", VT)

# Define a 3x3 matrix
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Compute the Singular Value Decomposition
U, S, VT = np.linalg.svd(A)

# Create the diagonal matrix  from the singular values
Sigma = np.zeros((3, 3))
np.fill_diagonal(Sigma, S)

# Reconstruct the original matrix
A_reconstructed = np.dot(U, np.dot(Sigma, VT))

print("Original matrix:\n", A)
print("Reconstructed matrix:\n", A_reconstructed)

