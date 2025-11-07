"""
In Pandas, function application means applying a custom or built-in function to your DataFrame or Series to process or transform the data.
It is mainly done using three methods: 

Table wise Function Application: pipe()
Row or Column Wise Function Application: apply()
Element wise Function Application: map()
"""

import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

print("Original DataFrame:",df)

# Apply a function to each column
print(df.apply(sum))

# Apply a custom function to each row
print(df.apply(lambda x: x.max() - x.min(), axis=1))

""" applymap()
Used only for DataFrames to apply a function 
element-wise (to each individual value).
"""
# Example:
# Square each element
print(df.applymap(lambda x: x**2))

"""
map()
Used only for Series (a single column) to apply a function, 
dictionary, or mapping.
"""
# Example:

s = pd.Series([1, 2, 3, 4])

# Apply a function
print(s.map(lambda x: x*10))

# Use dictionary mapping
print(s.map({1: 'A', 2: 'B', 3: 'C'}))