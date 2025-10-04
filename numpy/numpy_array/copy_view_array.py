"""
The Difference Between Copy and View

The main difference between a copy and a view of an array is that the copy 
is a new array, and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect 
original array, and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect 
the original array, and any changes made to the original array will affect the view.
"""
"""
View
A view is a new array object that is a reference to the original data.
 When you create a view, no new data is allocated; instead, 
 the new array shares the same memory as the original array. 
 This means that changes made to the view will affect the original array, 
 and vice versa.

Creating a View
You can create a view of an array by slicing it or using 
functions like np.reshape(). Here are some examples:
"""

import numpy as np

arr = np.array([1,2,3,4,5])


x = arr.copy()
x[2] = 9
print(arr)  # [1 2 3 4 5]
print(x)    # [1 2 9 4 5]

# original array does not change when we chane x array

# View 

y = arr.view()
y[2] = 0
print(y)    
print(arr)
# both print result are same because when we change view elements its change the original array too


