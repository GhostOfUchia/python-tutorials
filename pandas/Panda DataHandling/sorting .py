import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns = ['col2','col1'])

print("Original DataFrame:\n", unsorted_df)

# Sort the DataFrame by labels
sorted_df=unsorted_df.sort_index()
print("\nOutput Sorted DataFrame:\n", sorted_df)

# Sort the DataFrame by ascending order
sorted_df = unsorted_df.sort_index(ascending=False)
print("\nOutput Sorted DataFrame:\n", sorted_df)

unsorted_df = pd.DataFrame(np.random.randn(6,4),index=[1,4,2,3,5,0],columns = ['col2','col1', 'col4', 'col3'])

print("Original DataFrame:\n", unsorted_df)

# Sort the DataFrame columns
sorted_df=unsorted_df.sort_index(axis=1)
print("\nOutput Sorted DataFrame:\n", sorted_df)


# Sort the DataFrame by values
panda_series = pd.Series([18, 95, 66, 12, 55, 0])
print("Unsorted Pandas Series: \n", panda_series)

panda_series_sorted = panda_series.sort_values(ascending=True)
print("\nSorted Pandas Series: \n", panda_series_sorted)
