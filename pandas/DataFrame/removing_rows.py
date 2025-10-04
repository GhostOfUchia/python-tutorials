import pandas as pd
# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],'B': [4, 5, 6, 7, 8]},index=['r1', 'r2', 'r3', 'r4', 'r5'])

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Drop the row with index 3
# result = df.drop(3)

# Display the result
# print("\nAfter dropping the row at index 3:")
# print(result)

# Drop the rows by row-labels
# result = df.drop(['r1', 'r3'])

# Display the result
# print("\nAfter dropping the rows:")
# print(result)

# Dropping rows where column 'C' contains 0
result = df[df["B"] != 6]

# Display the result
print("\nAfter dropping the row where 'C' has 0:")
print(result)

# Drop the row using the index slicing
result = df.drop(df.index[2:4])

# Display the result
print("\nAfter dropping the row at 2 and 3:")
print(result)

# Create a DataFrame
d = pd.DataFrame({'A': [1, 2, 3, 4, 5],'B': [4, 5, 6, 7, 8]})

# Display original DataFrame
print("Original DataFrame:")
print(d)

# Drop the row using the index slicing
result = d.drop(d.index[2:3])

# Display the result
print("\nAfter dropping the row at 2 and 3:")
print(result)