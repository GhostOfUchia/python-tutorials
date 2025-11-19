import pandas as pd

# Creating the first DataFrame
left = pd.DataFrame({
'id': [1, 2, 3, 4, 5],
'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
'subject_id': ['sub1', 'sub2', 'sub4', 'sub6', 'sub5']
})
print("Left DataFrame:\n",left)



# Creating the second DataFrame
right = pd.DataFrame({
'id': [1, 2, 3, 4, 5],
'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
'subject_id': ['sub2', 'sub4', 'sub3', 'sub6', 'sub5']
})
print("\nRight DataFrame:\n",right)


# Merging DataFrames on a key 'id'
result = left.merge(right, on='id', how='inner', suffixes=('_left', '_right'))
# print(result)


# Merging on multiple keys 'id' and 'subject_id'
result2 = left.merge(right, on=['id', 'subject_id'])
# print(result2)

# Merging DataFrames using the left join method 
print(left.merge(right, on='subject_id', how='left'))

# Merging DataFrames using the right join method
print(left.merge(right, on='subject_id', how='right'))

# Merging the DataFrames using the outer join 
print(left.merge(right, how='outer', on='subject_id'))

# Merge the DataFrames using the inner join method
print(left.merge(right, on='subject_id', how='inner'))

# Merge the DataFrames using the join() method
result = left.join(right, lsuffix='_left', rsuffix='_right')
print(result)