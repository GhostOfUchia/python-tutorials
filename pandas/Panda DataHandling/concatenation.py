import pandas as pd

# Creating two DataFrames
one = pd.DataFrame({
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5'],
   'Marks_scored':[98,90,87,69,78]},
   index=[1,2,3,4,5])

two = pd.DataFrame({
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5'],
   'Marks_scored':[89,80,79,97,88]},
   index=[1,2,3,4,5])

# Concatenating DataFrames
result = pd.concat([one, two])
# print(result)

# Concatenating with Keys
# if you want to distinguish between the concatenated DataFrames, 
# you can use the keys parameter to associate specific keys with each 
# part of the DataFrame.

# print(pd.concat([one,two],keys=['x','y']))

# Ignoring Indexes During Concatenation

# print(pd.concat([one,two],keys=['x','y'],ignore_index=True))


# Concatenating Along Columns
# You can also concatenate DataFrames along columns by specifying axis=1.
# print(pd.concat([one,two],axis=1))