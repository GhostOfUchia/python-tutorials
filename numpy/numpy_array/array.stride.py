"""
🔹 What is a stride?

A stride tells NumPy how many bytes to move in memory to get to the next element 
along each axis.

Think of a NumPy array as a big block of memory.

Strides are like instructions: "how far to jump in memory 
to get the next row, column, etc."

Stride = memory jump per axis.

It depends on shape, data type (bytes per element), and slicing.

"""
import numpy as np

var1 = np.array([1,2,3,4])

# print(var1)  # [1 2 3 4]

# print(var1.strides) #  Output (on most systems, int64 = 8 bytes):(8,)

# The stride (8,) indicates that each element is 8 bytes apart in memory,
#  which is typical for an array of integers −


# d:\Downloads\output.png

var2 = np.array([[1,2,3],[4,5,6]])

# print("Var2 = ",var2) # Var2 =  [[1 2 3] [4 5 6]]

# print("Shape : ",var2.shape) # Shape :  (2, 3)

# print("Strides : ",var2.strides) # Strides :  (24, 8)

# The strides (24, 8) indicate that to move from one row to the next,
#  24 bytes are skipped, and to move from one column to the next,
#  8 bytes are skipped −

# Transposing the array changes the strides, reflecting 
# the new memory layout as shown in the example below −

var3 = np.array([[1,2,3],[4,5,6]])
var4 = var3.T   # transpose var3

# print(var3.shape) # shape (2,3)
# print(var4.shape) # shape(3,2)

# print(var3)  # [[1,2,3],[4,5,6]]
# print(var4)  #[[1,4],[2,5],[3,6]]

# print(var3.strides) #(24,8)
# print(var4.strides) #(8,24)

# What is np.zeros()?

# It creates a NumPy array filled with all zeros.
# Useful when you need an array of a certain size but with initial values = 0.

var5 = np.zeros((10,10))
var6 = var5[::4, 5]
"""
var5[::4, 5]

Here, var5 is probably a 2D NumPy array.
The slicing has two parts (before and after the comma):

::4 → row selection (first dimension)

: means "take all rows 
other wise if we give any number like 4,5,8 it can pic up specific index valve".

::4 means "take every 4th row starting from the beginning (index 0)".
4:: means take skip for row from started and take all back rows

5 → column selection (second dimension)

Just 5 means "take the element at column index 5".
"""


# print(var5.shape)
# print(var5)
# print(var6)

var5 = np.arange(60).reshape(10, 6)  # 10 rows, 6 columns
# print(var5)

# Apply slicing
result = var5[::4, :]
# print(result)
# 👉 Output (array first):


"""
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]
 [24 25 26 27 28 29]
 [30 31 32 33 34 35]
 [36 37 38 39 40 41]
 [42 43 44 45 46 47]
 [48 49 50 51 52 53]
 [54 55 56 57 58 59]]
👉 After slicing var5[::4, 5]:

css
Copy code
[ 5 29 53]
✔ Explanation:

::4 → take row 0, 4, 8, ...
:4 -> take first four row...
Column 5 → the last column in each selected row → values [5, 29, 53].

✅ So var5[::4, 5] means:
👉 "Pick every 4th row, but only the element from column index 5."

"""

# Strides in Multi-Dimensional Arrays

# Creating a 3D array
arr = np.arange(24).reshape(2, 3, 4)  # shape (2,3,4)
print("Array:\n", arr)
print("Shape:", arr.shape)
print("Strides:", arr.strides)

"""
How to Read These Strides

For shape = (2, 3, 4):

2 "blocks" (depth)

Each block has 3 rows

Each row has 4 columns

Strides = (96, 32, 8):

96 bytes → move to the next block (because each block = 3×4×8 = 96 bytes).

32 bytes → move to the next row inside a block (4 elements × 8 bytes each).

8 bytes → move to the next element in the row (1 element × 8 bytes).

"""
