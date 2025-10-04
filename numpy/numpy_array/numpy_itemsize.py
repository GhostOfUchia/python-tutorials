"""
NumPy Array Itemsize
The itemsize attribute in a NumPy array indicates the size, in bytes, 
of each element in the array. This size is determined by the data type of 
the array elements (e.g., integer, float).

By knowing the itemsize, you can estimate the total memory consumption of the array. 
This is important for understanding the memory layout and storage requirements of 
arrays, especially when dealing with large datasets.

You can access the itemsize of a NumPy array using the itemsize attribute.
 This attribute returns an integer representing the size (in bytes) of 
 each element in the array.

-> np.int8 has an itemsize of 1 byte.
-> np.int16 has an itemsize of 2 bytes.
-> np.float64 has an itemsize of 8 bytes.
-> np.complex128 has an itemsize of 16 bytes.

"""

import numpy as np
# int
var1 = np.array([1,2,3],dtype = np.int8)
var2 = np.array([1,2,3],dtype = np.int16)
var3 = np.array([1,2,3],dtype = np.int32)
var4 = np.array([1,2,3],dtype = np.int64)

# print(var1.itemsize) # 1byte
# print(var2.itemsize) # 2byte
# print(var3.itemsize) # 3byte
# print(var4.itemsize) # 4byte

# float
var5 = np.array([1.0,2.0,3.0],dtype = np.float16)
var6 = np.array([1.0,2.0,3.0],dtype = np.float32)
var7 = np.array([1.0,2.0,3.0],dtype = np.float64)

# print(var5.itemsize)
# print(var6.itemsize)
# print(var7.itemsize)

"""
Calculating Itemsize Memory Usage
To calculate the total memory occupied by the array, 
you can multiply the "itemsize" by the total number of elements in the array.

For example, if an array has "1000" elements and an itemsize of "8" bytes,
 the total memory used by the array would be "1000 * 8" = "8000" bytes.
"""

var6 = np.array([[1,2],[3,4]],dtype = np.int32)

totalbyte = var6.size* var6.itemsize

# print(totalbyte) # 4byte 
# 1 byte = 8bit  
# 32* 8 = 128
# 128/8 = 16

# Original array with int32
array_original = np.array([1, 2, 3], dtype=np.int32)
print(f"Original itemsize: {array_original.itemsize} bytes")

# Change data type to int8
array_new = array_original.astype(np.int8)
print(f"New itemsize: {array_new.itemsize} bytes")


