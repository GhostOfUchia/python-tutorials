import numpy as np

a = np.array([[1,2],[3,4]])
b = np. array([5,6])

c = np.linalg.solve(a,b)
print(c)

d = np.linalg.inv(a)

e = np.dot(b,d)
print (e)

"""
This method also produces the same result as the numpy.linalg.solve() function. 
However, using matrix inversion is more expensive and less stable for large matrices.
"""

# Define an overdetermined system (more equations than unknowns)
A = np.array([[1, 1], [2, 1], [3, 1]])
b = np.array([6, 8, 10])

# Solve the system using the least squares method
x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)

print("Solution vector x:", x)