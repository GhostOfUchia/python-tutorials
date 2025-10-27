import pandas as pd

# Creating a sample DataFrame
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'])

# Copy DataFrame to clipboard
df.to_clipboard()

# Read data from clipboard
clipboard_df = pd.read_clipboard()

# Display the DataFrame
print('DataFrame from clipboard:')
print(clipboard_df)

# Read clipboard content into a DataFrame
df2 = pd.read_clipboard(sep=',',header=None)
print(df2)

# Create a DataFrame
df3 = pd.DataFrame({
    "C1": [1, 2, 3], 
    "C2": [4, 5, 6], 
    "C3": ["a", "b", "c"]
}, index=["x", "y", "z"])

# Copies the DataFrame to the clipboard
df3.to_clipboard(sep=',')
print('DataFrame is successfully copied to the clipboard. Please paste it into any text editor or Excel sheet.')
print(df3)