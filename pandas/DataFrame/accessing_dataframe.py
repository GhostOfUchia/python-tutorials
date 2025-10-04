import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'Name': ['Steve', 'Lia', 'Vin', 'Katie'],
    'Age': [32, 28, 45, 38],
    'Gender': ['Male', 'Female', 'Male', 'Female'],
    'Rating': [3.45, 4.6, 3.9, 2.78]},
    index=['r1', 'r2', 'r3', 'r4'])

# Display the Input DataFrame
print('Input DataFrame:\n', df)

# Access the rows of the DataFrame
index_result = df.index
print('Output Accessed Row Labels:', index_result)

# Access the column of the dataframe
column_result = df.columns
print(column_result)

# Modify the Column labels of the DataFrame
df.columns = ['Col1', 'Col2', 'Col3', 'Col4']
print(df.columns)

# Modify the Row labels of the DataFrame
df.index = [100, 200, 300, 400]
print('Output Modified DataFrame with the updated index labels:\n', df)