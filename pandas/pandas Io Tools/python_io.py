import pandas as pd
import numpy as np
# Import StringIO to load a file-like object for reading CSV
from io import StringIO

# Create string representing CSV data
data = """S.No,Name,Age,City,Salary
1,Tom,28,Toronto,20000
2,Lee,32,HongKong,3000
3,Steven,43,Bay Area,8300
4,Ram,38,Hyderabad,3900"""

# Use StringIO to convert the string data into a file-like object
obj = StringIO(data)

# read CSV into a Pandas DataFrame
df = pd.read_csv(obj,index_col=['S.No'])

print(df)


# Create a string representing JSON data
data1 = """[
    {"Name": "Braund", "Gender": "Male", "Age": 30},
    {"Name": "Cumings", "Gender": "Female", "Age": 25},
    {"Name": "Heikkinen", "Gender": "Female", "Age": 35}
]"""

# Use StringIO to convert the JSON-formatted string data into a file-like object
obj1 = StringIO(data1)

# Read JSON into a Pandas DataFrame
df1 = pd.read_json(obj1, dtype={'Age': np.float64})
print(df1)

# Create string representing CSV data
data2 = """S.No,Name,Age,City,Salary
1,Tom,28,Toronto,20000
2,Lee,32,HongKong,3000
3,Steven,43,Bay Area,8300
4,Ram,38,Hyderabad,3900"""

# Use StringIO to convert the string data into a file-like object
obj2 = StringIO(data2)

# read CSV into a Pandas DataFrame
df2 = pd.read_csv(obj2, names=['a', 'b', 'c','d','e'], header=0)

# Display the DataFrame
print(df2)

# Create string representing CSV data
data4 = """S.No,Name,Age,City,Salary
1,Tom,28,Toronto,20000
2,Lee,32,HongKong,3000
3,Steven,43,Bay Area,8300
4,Ram,38,Hyderabad,3900"""

# Use StringIO to convert the string data into a file-like object
obj4 = StringIO(data4)
    
# read CSV into a Pandas DataFrame
df4 = pd.read_csv(obj4, skiprows=2)
print(df4)