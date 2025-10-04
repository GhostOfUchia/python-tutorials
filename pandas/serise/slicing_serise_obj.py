"""
Basics of Pandas Series Slicing
Series slicing can be done by using the [:] operator, 
which allows you to select subset of elements from the 
series object by specified start and end points.

Below are the syntax's of the slicing a Series −

Series[start:stop:step]: It selects elements from start to end with 
specified step value.

Series[start:stop]: It selects items from start to stop with step 1.

Series[start:]: It selects items from start to the rest of the object with step 1.

Series[:stop]: It selects the items from the beginning to stop with step 1.

Series[:]: It selects all elements from the series object.
"""
import numpy as np
import pandas as pd

data = np.array(['a','b','c','d','f'])
serise = pd.Series(data)
# print(serise)

# Slice the range of values
# result = serise[1:3]

# Display the output
# print('Values after slicing the Series:', result, sep='\n')

#retrieve the first three element
# print(serise[:3])

#retrieve the last three element
# print(serise[-3:])

s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

# Slice multiple elements
# print(s['a':'d'])

# Slice multiple elements
# print(s[:'c'])

se = pd.Series([1,2,3,4,5])

# Display the original series 
print("Original Series:\n",s)

# Modify the values of first two elements
s[:4] = [100, 200,300,400]

print("Series after modifying the first two elements:",s,sep = '\n')