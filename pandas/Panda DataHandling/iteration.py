import pandas as pd
import numpy as np
 
df = pd.DataFrame(np.random.randint(1,10,size=(4,3)),columns=['col1','col2','col3'])

print("Original DataFrame:\n", df)

# Iterate Through DataFrame rows

print("\nIterating through DataFrame rows:")

for key,value in df.items():
 print(key ,value)

# Iterate Through DataFrame rows
print("Iterated Output:")    

for key,value in df.iterrows():
 print(key ,value)

# Iterate Through DataFrame rows
print("Iterated Output:")
for row in df.itertuples():
   print(row)


# Iterate Through DataFrame Columns
print("Output:")
for col in df:
   print(col)


for index, row in df.iterrows():
   row['a'] = 10
print(df)   