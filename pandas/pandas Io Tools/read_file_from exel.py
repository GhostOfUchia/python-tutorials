from io import BytesIO
import pandas as pd
"""
# Read an Excel file
df = pd.read_excel('data.xlsx')

# Print the DataFrame
print('Output DataFrame:')
print(df)

# Read a specific sheet
df = pd.read_excel('data.xlsx', sheet_name="Sheet_2")

# Print the DataFrame
print('Output DataFrame:')
print(df)

# Read multiple sheets
df = pd.read_excel('data.xlsx', sheet_name=[0, 1])

# Print the DataFrame
print('Output Dict of DataFrames:')
print(df)

# Create a MultiIndex object
index = pd.MultiIndex.from_tuples([('A', 'one'), ('A', 'two'), ('B', 'one'), ('B', 'two')])

# Create a DataFrame
data = [[1, 2], [3, 4], [5, 6], [7, 8]]
df = pd.DataFrame(data, index=index, columns=['X', 'Y'])

df.to_excel("multiindex_data.xlsx")

# Read MultiIndex rows and columns
df = pd.read_excel("multiindex_data.xlsx", index_col=[0, 1])

print('Output DataFrame from Excel File:')
print(df)
"""
"""
#  Write DataFrame to an Excel file
# Create a DataFrame
df = pd.DataFrame([[5, 2], [4, 1]],index=["One", "Two"],columns=["Rank", "Subjects"])

# Display the DataFrame
print("DataFrame:\n", df)

# Export DataFrame to Excel
df.to_excel('Basic_example_output.xlsx')

print('The Basic_example_output.xlsx file is saved successfully..')

df1 = pd.DataFrame(
   [[5, 2], [4, 1]],
   index=["One", "Two"],
   columns=["Rank", "Subjects"]
)

df2 = pd.DataFrame(
   [[15, 21], [41, 11]],
   index=["One", "Two"],
   columns=["Rank", "Subjects"]
)

print("DataFrame 1:\n", df1)
print("DataFrame 2:\n", df2)

with pd.ExcelWriter('output_multiple_sheets.xlsx') as writer:
	df1.to_excel(writer, sheet_name='Sheet_name_1')
	df2.to_excel(writer, sheet_name='Sheet_name_2')

print('The output_multiple_sheets.xlsx file is saved successfully..')

# Create a new DataFrame
df3 = pd.DataFrame([[51, 11], [21, 38]],index=["One", "Two"],columns=["Rank", "Subjects"])

# Append the DataFrame to an existing Excel file
with pd.ExcelWriter('output_multiple_sheets.xlsm', mode='a') as writer:
    df3.to_excel(writer, sheet_name='Sheet_name_3', index=False)

print('The output_multiple_sheets.xlsm file is saved successfully with the appended sheet..')

df = pd.DataFrame(
[[5, 2], [4, 1]],
index=["One", "Two"],
columns=["Rank", "Subjects"])

print("Input DataFrame :\n", df)

# Create a BytesIO object
bio = BytesIO()

# Write the DataFrame to the BytesIO buffer
df.to_excel(bio, sheet_name='Sheet1')

# Get the Excel file from memory
bio.seek(0)
excel_data = bio.read()

print('\nThe Excel file is saved in memory successfully..')


df = pd.DataFrame(
   [[5, 2], [4, 1]],
   index=["One", "Two"],
   columns=["Rank", "Subjects"]
)

# Write DataFrame using xlsxwriter engine
df.to_excel('output_xlsxwriter.xlsx', sheet_name='Sheet1', engine='xlsxwriter')

print('The output_xlsxwriter.xlsx is saved successfully..')
"""