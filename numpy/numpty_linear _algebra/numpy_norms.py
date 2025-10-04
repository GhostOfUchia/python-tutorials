import numpy as np

"""
✅ Quick Recap of Matrix Norms in NumPy:

np.linalg.norm(A, 'fro') → Frobenius Norm

np.linalg.norm(A, 1) → 1-Norm (max column sum)

np.linalg.norm(A, np.inf) → ∞-Norm (max row sum)

np.linalg.norm(A, 2) → 2-Norm (largest singular value)
"""

# Frobenius Norm

arr = np.array([[1,2],[3,4]])

fro_norm = np.linalg.norm(arr,'fro')
# Step by Step Calculation for Matrix A:
# 1² + 2² + 3² + 4² = 1 + 4 + 9 + 16 = 30
# √30 ≈ 5.4772

#So, Frobenius norm = 5.4772
print("Forbenius Norms is =",fro_norm)
# In short:

# It’s like the Euclidean norm but for a whole matrix.

# Just square all numbers → add → square root. ✅

# 1-Norm Using NumPy
one_norm = np.linalg.norm(arr,1) 

#Column 1: |1| + |3| = 1 + 3 = 4
#Column 2: |-2| + |4| = 2 + 4 = 6
# Max column sum = 6
# So, 1-Norm = 6

print("1-Norm is ",one_norm)

# Infinity Norm Using NumPy

inf_norm = np.linalg.norm(arr,np.inf)

"""
Row 1: |1| + |2| = 1 + 2 = 3

Row 2: |3| + |4| = 3 + 4 = 7

👉 Max row sum = 7

So, ∞-Norm = 7
"""
print("Infinet Norm is ",inf_norm)

# 2-Norm Using NumPy

two_norm = np.linalg.norm(arr,2)

"""
Compute singular values of 
𝐴
A (using SVD).

The largest singular value = 2-Norm.

👉 For this matrix, NumPy will calculate:
Largest singular value ≈ 4.9193

So, 2-Norm = 4.9193
"""
print("2-Norm is ",two_norm)

