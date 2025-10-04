"""
Data Types in NumPy
NumPy has some extra data types, and refer to data types with one character, 
like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

"""
import numpy as np

arr =  np.array([1,2,3,4,5])
#print(arr.dtype)   # int64

arr_String = np.array(["Amit","Pooja","Raghav","Naman"],dtype = np.str_)
# print(arr_String.dtype) <U6

"""
What if a Value Can Not Be Converted?
If a type is given in which elements can't be casted then NumPy will raise a ValueError.

ValueError: In Python ValueError is raised when the type of passed argument to a function is unexpected/incorrect.

Example
A non integer string like 'a' can not be converted to integer (will raise an error):

import numpy as np

arr = np.array(['a', '2', '3'], dtype='i')
Converting Data Type on Existing Arrays
The best way to change the data type of an existing array, 
is to make a copy of the array with the astype() method.

The astype() function creates a copy of the array, 
and allows you to specify the data type as a parameter.

The data type can be specified using a string, like 'f' for float, 'i' for integer etc. 
or you can use the data type directly like float for float and int for integer."""

arr2 = np.array([1.1,2.1,3.1,4.1])
new_arr2 = arr2.astype('i')   
new_arr3 = new_arr2.astype(float)
print(new_arr2.dtype)
print(new_arr3.dtype)


"""
In NumPy, a powerful library for numerical computations in Python, data types (often abbreviated as "dtype") define the kind of data that can be stored in a NumPy array. Understanding the different data types is crucial for efficient memory usage and performance.

Common Data Types in NumPy
Integer Types:

np.int8: 8-bit integer
np.int16: 16-bit integer
np.int32: 32-bit integer
np.int64: 64-bit integer
np.uint8: Unsigned 8-bit integer
np.uint16: Unsigned 16-bit integer
np.uint32: Unsigned 32-bit integer
np.uint64: Unsigned 64-bit integer
Floating Point Types:

np.float16: Half precision (16-bit) float
np.float32: Single precision (32-bit) float
np.float64: Double precision (64-bit) float (default float type in NumPy)
Complex Types:

np.complex64: Complex number represented by two 32-bit floats
np.complex128: Complex number represented by two 64-bit floats (default complex type)
Boolean Type:

np.bool_: Boolean type (True or False)
String Types:

np.str_: String type (variable length)
np.bytes_: Byte string type (fixed length)
Object Type:

np.object_: General-purpose type for Python objects
Datetime and Timedelta Types:

np.datetime64: For datetime representation
np.timedelta64: For time duration representation
Creating Arrays with Specific Data Types
You can specify the data type when creating a NumPy array using the dtype argument:

import numpy as np

# Creating an array of integers
arr_int = np.array([1, 2, 3], dtype=np.int32)

# Creating an array of floats
arr_float = np.array([1.0, 2.0, 3.0], dtype=np.float64)

# Creating an array of strings
arr_str = np.array(['a', 'b', 'c'], dtype=np.str_)

# Creating an array of booleans
arr_bool = np.array([True, False, True], dtype=np.bool_)
Checking the Data Type of an Array
You can check the data type of a NumPy array using the .dtype attribute:

print(arr_int.dtype)   # Output: int32
print(arr_float.dtype) # Output: float64
print(arr_str.dtype)   # Output: <U1 (Unicode string of length 1)
Changing the Data Type of an Array
You can use the .astype() method to change the data type of an existing array:

arr_float_to_int = arr_float.astype(np.int32)
print(arr_float_to_int) # Output will be converted to integers
Understanding and using data types properly can lead to better performance and memory efficiency in your numerical applications using NumPy.
"""