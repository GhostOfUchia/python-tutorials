import pandas as pd
# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3],'B': [4, 5, 6]},index=['x', 'y', 'z'])

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Rename column 'A' to 'aa'
df = df.rename(columns={'A': 'aa'})

# Display modified DataFrame
print("Modified DataFrame:")
print(df)

# Renaming Row Labels in a DataFrame

# Rename the multiple row labels
df = df.rename(index={'x': 'r1', 'y':'r2', 'z':'r3'})

# Display modified DataFrame
print("Modified DataFrame:")
print(df)

# Add a new column 'C' with values
df['C'] = [7, 8, 9]

# Display updated DataFrame
print("DataFrame after adding a new column 'C':")
print(df)

# Insert a new column 'D' at position 1
df.insert(1, 'D', [10, 11, 12])

# Display updated DataFrame
print("DataFrame after inserting column 'D' at position 1:")
print(df)

# Replace the contents of column 'A' with new values
df['aa'] = [10, 20, 30]

# Display updated DataFrame
print("DataFrame after replacing column 'A':")
print(df)

# Replace the contents 
df.replace({'aa': 1, 'B': 6}, 100, inplace=True)

# Display updated DataFrame
print("DataFrame after replacing column 'A':")
print(df)

# Delete columns 'A' and 'B'
df = df.drop(columns=['aa', 'B'])

# Display updated DataFrame
print("DataFrame after deleting columns 'A' and 'B':")
print(df)