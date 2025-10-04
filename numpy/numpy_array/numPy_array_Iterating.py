import numpy as np

# iterating One-d array

arr = np.array([1,2,3,4,5])

for x in arr:
    print(x)

# iterating 2-d array
arr2 = np.array([[1,2,3,4],[5,6,7,8]]) 

for y in arr2:
    for z in y:
        print(z)

# The function nditer() is a helping function that can be used from very basic to very advanced iterations. It solves 
# some basic issues which we face in iteration, lets go through it with examples.        

for n in np.nditer(arr2):
    print(n)

# Iterate through every scalar element of the 2D array skipping 1 element:
for n in np.nditer(arr2[:,::2]):
    print(n)


for m in np.nditer(arr2 ,flags=['buffered'], op_dtypes=['S']):
    print(m)    

"""
    Enumeration means mentioning sequence number of somethings one by one.
   Sometimes we require corresponding index of the element while iterating, 
   the ndenumerate() method can be used for those usecases.    
                                                              """
for idx,a in np.ndenumerate(arr2):
    print(idx, a)

arr = np.arange(1, 13).reshape(3, 4)  # 3 rows, 4 columns
print("Original array:\n", arr)

# Iterate row by row
print("\nRow-wise:")
for x in np.nditer(arr, order='C'):
    print(x, end=" ")

# Iterate column by column
print("\n\nColumn-wise:")
for x in np.nditer(arr, order='F'):
    print(x, end=" ")

# ✅ Key Point:

# order='C' → row-major (default in Python/NumPy).

# order='F' → column-major (like Fortran/Matlab).        