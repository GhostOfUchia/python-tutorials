"""
Aggregation means summarizing data — reducing many values to a single summary 
value (like sum, mean, count, etc.).

👉 In pandas, aggregation is used to compute summary statistics for 
each column or for each group of data.
"""

import pandas as pd

df = pd.DataFrame({
   # 'Team': ['A', 'A', 'B', 'B', 'C'],
    'Points': [10, 20, 15, 25, 30],
    'Assists': [5, 7, 8, 10, 6]
})
print("Original DataFrame:",df)

# ✅ Example 1: Aggregate the whole DataFrame
result = df.agg(['sum', 'mean'])
print(result)

# ✅ Example 2: Aggregate specific columns with different functions
result2 = df.agg({'A': ['sum', 'min'], 'B': ['min', 'max']})
print("\nResults:\n",result2)