from json import dumps, loads

import pandas as pd
from io import StringIO

# 1 - reading JSON files with Pandas
# Create a string representing JSON data
data = """[
    {"Name": "Braund", "Gender": "Male", "Age": 30},
    {"Name": "Cumings", "Gender": "Female", "Age": 25},
    {"Name": "Heikkinen", "Gender": "Female", "Age": 35}
]"""

# Use StringIO to convert the JSON formatted string data into a file-like object
obj = StringIO(data)

# Read JSON into a Pandas DataFrame
df = pd.read_json(obj)

print(df)

# 2 writing JSON files with Pandas
 
# Create a DataFrame from the above dictionary
df = pd.DataFrame({"Name":["Braund", "Cumings", "Heikkinen"], 
"Gender": ["Male", "Female", "Female"],
"Age": [30, 25, 25]})
print("Original DataFrame:\n", df)    

# Write DataFrame to a JSON file
df.to_json("output_written_json_file.json", orient='records', lines=True)

print("The output JSON file has been written successfully.")

# 3 Writing a JSON file using the split orientation

# Create a DataFrame
df = pd.DataFrame(
    [["x", "y"], ["z", "w"]],
    index=["row_1", "row_2"],
    columns=["col_1", "col_2"],
)

# Convert DataFrame to JSON with 'split' orientation
result = df.to_json(orient="split")
parsed = loads(result)

# Display the JSON output
print("JSON Output (split orientation):")
print(dumps(parsed, indent=4))

