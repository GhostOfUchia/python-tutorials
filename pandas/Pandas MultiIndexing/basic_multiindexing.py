import pandas as pd
import numpy as np
"""

# Create a 2D list
list_2d = [["BMW", "BMW", "Lexus", "Lexus", "foo", "foo", "Audi", "Audi"],
["1", "2", "1", "2", "1", "2", "1", "2"]]

# Create a MultiIndex object
index = pd.MultiIndex.from_arrays(list_2d, names=["first", "second"])

# Creating a MultiIndexed Series
s = pd.Series(np.random.random_integers(80, size=8), index=index)

#Display the output Series 
print("Output MultiIndexed Series:\n",s)

"""

"""
#Create a MultiIndex object
tuples = list(zip(*list_2d ))
print(tuples)
index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])

 Creating a MultiIndexed DataFrame
df = pd.DataFrame(np.random.randint(1,100,size=(8, 4)), index=index, columns=["A", "B", "C", "D"])

 Display the output Series 
print("Output MultiIndexed DataFrame:\n", df)

"""

"""
#               Creating MultiIndex Using from_product()

# Create a list of lits 
iterable = [[1, 2, 3], ['green', 'black']]

# Create a MultiIndex object
index = pd.MultiIndex.from_product(iterable, names=["number", "color"])

# Creating a MultiIndexed DataFrame
df = pd.DataFrame(np.random.randint(1,100,size=(6, 3)), index=index, columns=["A", "B", "C"])

# Display the output Series 
print("Output MultiIndexed DataFrame:\n", df)

"""

"""
#       Creating MultiIndex from DataFrame
# Create a DataFrame
df = pd.DataFrame([["BMW", 1], ["BMW", 2], ["Lexus", 1],["Lexus", 2]], 
 columns=["first", "second"])

# Create a MultiIndex object
index = pd.MultiIndex.from_frame(df)

# Creating a MultiIndexed DataFrame
df = pd.DataFrame(np.random.randint(1,10,size=(4,3)), index=index, columns=["A", "B", "C"])

# Display the output Series 
print("Output MultiIndexed DataFrame:\n", df)

"""

"""
Basic Indexing on Axis with MultiIndex 

"""
# Creating MultiIndex from arrays
arrays = [["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
["one", "two", "one", "two", "one", "two", "one", "two"]]

# Creating a list of tuples from the arrays
tuples = list(zip(*arrays))

# Creating a MultiIndex from tuples
index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])

# Creating a Series with MultiIndex
s = pd.Series([2, 3, 1, 4, 6, 1, 7, 8], index=index)

print("MultiIndexed Series:\n", s)

# Indexing the MultiIndexed Series using .loc[]
print("\nSelecting data at index ('bar', 'one') and column 'A':")
print(s.loc[('bar', 'one')])
