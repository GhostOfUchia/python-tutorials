"""
In mathematics, the mean is the average value of a set of numbers. 
The most common type is the arithmetic mean, 
which is the sum of the numbers divided by the count of the numbers.

Other types include the geometric mean (nth root of the product of the numbers) 
and the harmonic mean (number of values divided by the sum of reciprocals).

These different means are used based on the nature of the data and specific 
needs of the analysis.


Basic signature:
np.mean(a, axis=None, dtype=None, out=None, keepdims=False)
"""
import numpy as np

int_arr = np.array([1,2,4,5]) 
# 1+2+4+5 = 12/4 = 3
mean_nalue = np.mean(int_arr)
print(mean_nalue)   # 3

# define a 2d array
two_d_arr = np.array([[1,2,3],[4,5,6]])
# mean row wise 
two_d_mean_value = np.mean(two_d_arr,axis = 1)

# mean column wise
two_d_mean_value_column = np.mean(two_d_arr,axis = 0)

print(two_d_mean_value)
print(two_d_mean_value_column)

# Calculating Mean with a Specified Data Type\

# Define an array of integers
arr_int = np.array([10, 20, 30,40])

# Calculate the mean with a specified data type (float64)
mean_float = np.mean(arr_int, dtype=np.float64)

print("Mean with dtype float64:", mean_float)

# Define a 2D array 
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Mean along columns while keeping dimensions
mean_keepdims = np.mean(arr_2d, axis=1, keepdims=True)

print("Mean with keepdims=True:", mean_keepdims)

