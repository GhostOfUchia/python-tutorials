import numpy as np

# Define a 2x2 matrix
A = np.array([[4, -2], 
              [1,  1]])

# Compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Define a 3x3 matrix
B = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])

# Compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(B)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Define a symmetric matrix
C = np.array([[4, 1, 1],
              [1, 4, 1],
              [1, 1, 4]])

# Compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(C)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Define a matrix
D = np.array([[2, 0, 0],
              [1, 3, 0],
              [4, 5, 6]])

# Compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(D)

# Diagonal matrix of eigenvalues
D_diag = np.diag(eigenvalues)

# Reconstruct the original matrix
reconstructed_D = eigenvectors @ D_diag @ np.linalg.inv(eigenvectors)

print("Original matrix:\n", D)
print("Reconstructed matrix:\n", reconstructed_D)