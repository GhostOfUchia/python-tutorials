"""
What is Broadcasting in NumPy?

In NumPy, broadcasting means automatically stretching arrays of different shapes 
so they can be used together in operations (like addition, multiplication, etc.) 
without making extra copies.

It’s a way for NumPy to apply operations on arrays of different sizes element-wise.

******************   Broadcasting Rules  ***************         

Two arrays can be broadcast together if:

Compare shapes from right to left.

Dimensions must be:

Equal, OR

One of them is 1, OR

Missing (treated as 1).

If not, error → ValueError: operands could not be broadcast together.
"""

import numpy as np

var1 = np.array([1,2,3]) # shape (3,)
var2 = 5              #scaler

var3 = var1+var2   # Here, b (a scalar) is broadcasted to [5, 5, 5] automatically.
#  print(var3)   # [6 7 8]

# Another Example 2-d +1d

var4 = np.array([[1,2,3],[4,5,6]])  # shape (2,3)
var5= np.array([10,20,30])         # shape(3,)

var6 = var4+var5

# print(var6)   [[11 22 33][14 25 36]]

"""
  A has shape (2, 3)

  B has shape (3,)

  NumPy stretches B into shape (2, 3) → [[10,20,30], [10,20,30]]
"""

# Example with 2D and Column Vector

var7 = np.array([[1,2,3],[4,5,6]]) # shape(2,3)
var8 = np.array([[10],[20]])       # shape(2,1)

var9 = var7+var8   
# NumPy stretches var8 into shape [10,10,10][20,20,20]
# print(var9)   [[11 12 13] [24 25 26]]

# Broadcasting with Multi-Dimensional Arrays

var10 = np.array((10,20,30))  # shape (3,)
var11 = np.arange(3)  # it created [0 1 2]
"""
It creates an array with numbers in a given range, 
similar to Python’s built-in range(), 
but it gives you a NumPy array instead of a list.

Syntax
numpy.arange(start, stop, step, dtype=None)


start → beginning value (default = 0)

stop → end value (exclusive, not included)

step → difference between numbers (default = 1)

dtype → type of array elements (optional)
"""
var12 = var10+var11
# print(var11.shape)  shape (3,)
# print(var10.shape) # shape(3,)
# print(var12)    [10 21 32]
# print(var12.shape)  (3,)

# Applying Functions with Broadcasting
"""
Mathematical Functions: Functions that perform mathematical operations, 
such as addition, subtraction, multiplication, and division.

Statistical Functions: Functions that compute statistical properties, 
like mean, median, variance, and standard deviation.

Reduction Functions: Functions that reduce the dimensions of an array 
by performing operations such as sum, product, or maximum.

Logical Operations: Functions that perform logical operations, 
such as comparisons and logical operations (e.g., AND, OR, NOT).

"""

var13 = np.array([[1,2,3],[4,5,6]]) # shape (2,3)
var14 = np.array([[10],[20]])   # shape (2,)

maxresult = np.maximum(var13,var14)
# when we performe maximum  function broadcasting stretching 
# var14 (2,) in to (2,3) [[10 10 10],[20 20 20]]

minresult = np.minimum(var13,var14)

print(maxresult)  # [[10 10 10],[10 10 10]]

print(minresult)  # [[1 2 3][4 5 6]]