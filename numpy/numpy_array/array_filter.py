import numpy as np
"""
Getting some elements out of an existing array and creating a new array 
out of them is called filtering.

In NumPy, you filter an array using a boolean index list.

A boolean index list is a list of booleans corresponding to indexes in the array.

If the value at an index is True that element is contained in the filtered array, 
if the value at that index is False that element is excluded from the filtered array.


✅ Summary:

arr[condition] → basic way (boolean mask)

np.isin() → filter by membership

np.nonzero() → filter non-zeros


"""
arr = np.array([41, 42, 43, 44,47])

x = [True, False, True, False,True]

newarr = arr[x]

print(newarr)
#The example above will return [41, 43,47], why?
#Because the new array contains only the values where 
# the filter array had the value True, in this case, index 0 and 2.

#In the example above we hard-coded the True and False values, 
# but the common use is to create a filter array based on conditions.

arr2 = np.array([41,42,43,44,45,46,47])

filtered_array = [] # create a empety array

for elements in arr2:  # go through each elements of array
    if elements <= 44:  
        filtered_array.append(True)
    else:
        filtered_array.append(False)

new_array = arr2[filtered_array]

print(new_array)
print(filtered_array)

# Create a filter array that will return only even elements from the original array:

arr3 = np.array([1,2,3,4,5,6,7,8,9])

filter_array = []

for elements in arr3:
    if elements %2 == 0:
       filter_array.append(True)
    else:
        filter_array.append(False)  

sort_array = arr3[filter_array]

print(filter_array)
print(sort_array)

# Creating Filter Directly From Array

#The above example is quite a common task in NumPy and NumPy 
# provides a nice way to tackle it.

#We can directly substitute the array instead of the iterable 
# variable in our condition and it will work just as we expect it to.      
arr4 = np.array([41, 42, 43, 44])

filt_arr = arr4 > 42
fil_arr = arr4 % 2 == 0

newar = arr4[filt_arr]
nearr = arr4[fil_arr]

print(filt_arr)   # [False False  True  True]
print(newar)      # [43 44]
print(fil_arr)    # [False  True False  True]
print(nearr)      # [42 44]

#            1. Filtering with conditions
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Select only values greater than 25
filtered = arr[arr > 25]
print(filtered)   # [30 40 50]


# 👉 arr > 25 creates a boolean mask → [False False True True True]
# 👉 Using it on arr filters the matching elements.

#       2. Filter with multiple conditions
arr = np.array([5, 10, 15, 20, 25, 30])

# Between 10 and 25
filtered = arr[(arr >= 10) & (arr <= 25)]
print(filtered)   # [10 15 20 25]


# 👉 Use & for AND, | for OR, ~ for NOT.

#      3. Filtering with np.isin()
arr = np.array([10, 20, 30, 40, 50])

# Keep only elements that are in [20, 50]
filtered = arr[np.isin(arr, [20, 50])]
print(filtered)   # [20 50]


#     4. Filtering Non-zeros (np.nonzero)
arr = np.array([0, 7, 0, 8, 0,9])

filtered = arr[np.nonzero(arr)]
print(filtered)   # [7 8 9]

#     5. Filtering in 2D arrays
arr2d = np.array([[1, 2, 3,7], [4, 5, 6,9]])

# Get elements greater than 3
filtered = arr2d[arr2d > 3]
print(filtered)   # [7 4 5 6 9]