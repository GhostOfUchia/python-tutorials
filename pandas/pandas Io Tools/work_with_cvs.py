import pandas as pd

# Import StringIO to load a file-like object for reading CSV
from io import StringIO

# Create string representing CSV data
data = """Name,Gender,Age
Braund,male,22
Cumings,female,38
Heikkinen,female,26
Futrelle,female,35"""

# Use StringIO to convert the string data into a file-like object
obj = StringIO(data)

# read CSV into a Pandas DataFrame
df = pd.read_csv(obj)

print(df)

# dictionary of lists
d = {'Car': ['BMW', 'Lexus', 'Audi', 'Mercedes', 'Jaguar', 'Bentley'],
'Date_of_purchase': ['2024-10-10', '2024-10-12', '2024-10-17', '2024-10-16', '2024-10-19', '2024-10-22']}

# creating dataframe from the above dictionary of lists
dataFrame = pd.DataFrame(d)
print("Original DataFrame:\n",dataFrame)

# write dataFrame to SalesRecords CSV file
dataFrame.to_csv("Output_written_CSV_File.csv")

# display the contents of the output csv
print("The output csv file written successfully...")