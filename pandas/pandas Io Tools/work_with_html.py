import pandas as pd
from io import StringIO


# Read HTML table from a URL
url = "https://www.tutorialspoint.com/sql/sql-clone-tables.htm"
tables = pd.read_html(url)

# Access the first table from the URL
df = tables[0]

# Display the resultant DataFrame
print('Output First DataFrame:', df.head())

#Reading HTML data from a string
 
# Create an HTML string
html_str = """
<table>
   <tr><th>C1</th><th>C2</th><th>C3</th></tr>
   <tr><td>a</td><td>b</td><td>c</td></tr>
   <tr><td>x</td><td>y</td><td>z</td></tr>
</table>
"""

# Read the HTML string
dfs = pd.read_html(StringIO(html_str))
print(dfs[0])

# Create an HTML string
html_str = """
<table>
   <tr><th>C1</th><th>C2</th><th>C3</th></tr>
   <tr><td>a</td><td>b</td><td>c</td></tr>
   <tr><td>x</td><td>y</td><td>z</td></tr>
</table>
"""
# handling Multiple table from html file

# Save to a temporary file and read
with open("temp.html", "w") as f:
    f.write(html_str)

df = pd.read_html("temp.html")[0]
print(df)

# Read tables from a SQL tutorial
url = "https://www.tutorialspoint.com/sql/sql-clone-tables.htm"
tables = pd.read_html(url, match='Field')

# Access the table
df = tables[0]
print(df.head())

# writing dataframe to html file

# Create a DataFrame
df = pd.DataFrame([[1, 2], [3, 4]], columns=["A", "B"])

# Convert the DataFrame to HTML table
html = df.to_html()

# Display the HTML string
print(html)