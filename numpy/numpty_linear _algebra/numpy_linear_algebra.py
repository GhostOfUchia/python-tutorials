"""
Linear algebra is a branch of mathematics that deals with vectors, matrices, 

and linear transformations.

NumPy package contains numpy.linalg module that provides all the functionality 

required for linear algebra. Some of the important functions in this module 

are described in the following table.

"""
import numpy as np

# Creating a 2x3 matrix
matrix = np.array([[1, 2, 3], [4, 5, 6]])
# print("Matrix:\n", matrix)


a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Matrix Addition
C = a+b
# print("Matrix Addition:\n", C)

# Matrix Subtraction
D = a-b
# print("Matrix Subtraction:\n", D)

# Matrix Multiplication
#  we are performing matrix multiplication on two 2x2 NumPy arrays, 
# A and B, using the @ operator and the np.dot() function −

var1 = np.array([[1, 2], [3, 4]])
var2 = np.array([[5, 6], [7, 8]])

# Matrix Multiplication
var3 = var1 @ var2
# print("Matrix Multiplication with @:\n", var3)

var4 = np.dot(a, b)
# print("Matrix Multiplication with np.dot():\n", var4)


# Matrix Transpose

var5 = np.array([[1,2,3],[4,5,6]])
var6 = var5.T

# print("Before Transpose",var5)
# print("After Transpose",var6)

"""
🔹 1. Determinant in NumPy

The determinant tells us certain properties of a square matrix:

If det(A) = 0, the matrix is singular (no inverse exists).

If det(A) ≠ 0, the matrix is invertible.

👉 In NumPy, we use numpy.linalg.det().


"""
# 2*2 array
arr =  np.array([[1,2],[3,4]])
det = np.linalg.det(arr)

# print(det)

# 3*3 matrix
aar2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
det2 = np.linalg.det(aar2)
# formula = det(A)=a(ei−fh)−b(di−fg)+c(dh−eg)
# print(det2)


# Inverse
#2*2
arr3= np.array([[1,2],[3,4]])
inv = np.linalg.inv(arr3)
# print(inv)

"""
What is an Eigenvalue and Eigenvector?

Imagine a matrix 
𝐴
A is like a transformation machine that stretches, rotates, or squishes vectors.
Most vectors change direction + length when multiplied by 
𝐴
A.

But some special vectors only get stretched or 
squished (their direction doesn’t change).

👉 These are called Eigenvectors.
👉 The factor by which they are stretched is the Eigenvalue.
"""

eigenvalue = np.linalg.eig(arr)
print(eigenvalue)

"""
A linear system is a collection of linear equations with one or more unknowns.

👉 Example (2 equations, 2 unknowns):
2x+y=5
x−y=1

Here, we want to find values of x and y that satisfy both equations at the same time.
"""

A = np.array([[3, 1], [1, 2]])
B = np.array([9, 8])

solution = np.linalg.solve(A,B)
# print(solution)

# Singular Value Decomposition (SVD)

A1 = np.array([[3, 1],[1, 3],[1, 1]])

sld = np.linalg.svd(A1)
# print(A1)

# 

A = np.array([[1, 2],[3, 4]])

# Norms
norm_f = np.linalg.norm(A, 'fro')     # Frobenius norm
norm_2 = np.linalg.norm(A, 2)         # Spectral (2-norm)
norm_inf = np.linalg.norm(A, np.inf)  # Infinity norm

# Condition number

"""
A norm is just a way of measuring the "size" or "length" of a vector or matrix.
It’s like the distance formula for vectors, but more general.
"""
cond_num = np.linalg.cond(A)

print("Frobenius norm:", norm_f)
print("2-norm:", norm_2)
print("Infinity norm:", norm_inf)
print("Condition number:", cond_num)

d = np.array([[1, 2], [3, 4]])

# Condition number
# The condition number of a matrix tells us how stable or unstable 
# it is for solving linear systems.

cond = np.linalg.cond(d)
print("Condition number of A:", cond)