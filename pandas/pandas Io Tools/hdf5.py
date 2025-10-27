import pandas as pd
import numpy as np

# Create the store using the HDFStore class
store = pd.HDFStore("store.h5")

# Display the store
print(store)

# It is important to close the store after use
#store.close()

# Create the data 
index = pd.date_range("1/1/2024", periods=8)
s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=["A", "B", "C"])

# Write Pandas data to the Store, which is equivalent to store.put('s', s)
store["s"] = s  
store["df"] = df

# Read Data from the store, which is equivalent to store.get('df')
from_store = store["df"]
from_store_s = store["s"]
print('Retrieved Data From the HDFStore:\n',from_store)
print('Retrieved Data From the HDFStore:\n',from_store_s)

# Close the store after use
store.close()

# Writing and Reading HDF5 files using to_hdf() and read_hdf()
# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]},index=['x', 'y', 'z']) 

# Write data to an HDF5 file using the to_hdf()
df.to_hdf("data_store.h5", key="df", mode="w", format="table")

print("Data successfully written to HDF5 file")

# Read data from the HDF5 file using the read_hdf()
retrieved_df = pd.read_hdf("data_store.h5", key="df")

# Display the retrieved data
print("Retrieved Data:\n", retrieved_df.head())

# Appending Data to HDF5 Files Using to_hdf()
# Create a DataFrame to append
df_new = pd.DataFrame({'A': [7, 8], 'B': [1, 1]},index=['i', 'j'])

# Append the new data to the existing HDF5 file
df_new.to_hdf("data_store.h5", key="df", mode="a", format="table", append=True)

print("Data successfully appended")

# Now read data from the HDF5 file using the read_hdf()
retrieved_df = pd.read_hdf("data_store.h5", key='df')

# Display the retrieved data
print("Retrieved Data:\n", retrieved_df.head())