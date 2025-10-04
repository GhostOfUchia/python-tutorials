import numpy as np
data_odd = np.array([1, 3, 5, 7, 9])
data_even = np.array([1, 3, 5, 7])

# Calculating the median for both datasets
median_odd = np.median(data_odd)
median_even = np.median(data_even)

print("Median of odd dataset:", median_odd)
print("Median of even dataset:", median_even)

# Create a 2D array
data_2d = np.array([[1, 3, 5], [2, 4, 6], [7, 8, 9]])

# Calculate the median along axis 0 (columns)
median_axis_0 = np.median(data_2d, axis=0)

# Calculate the median along axis 1 (rows)
median_axis_1 = np.median(data_2d, axis=1)

print("Median along axis 0:", median_axis_0)
print("Median along axis 1:", median_axis_1)

# Create a 3D array
data_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Median along axis 0
median_3d_axis_0 = np.median(data_3d, axis=0)

# Median along axis 1
median_3d_axis_1 = np.median(data_3d, axis=1)

# Median along axis 2
median_3d_axis_2 = np.median(data_3d, axis=2)

print("Median along axis 0:", median_3d_axis_0)
print("Median along axis 1:", median_3d_axis_1)
print("Median along axis 2:", median_3d_axis_2)

"""
Axis=0 → Compare the same positions across the two blocks.

Axis=1 → Compare the rows inside each block.

Axis=2 → Compare the columns inside each row.

"""
# Create an array with NaN values
data_with_nan = np.array([1, 3, np.nan, 5, 7])

# Calculate the median while ignoring NaN values
median_without_nan = np.nanmedian(data_with_nan)

print("Median without NaN:", median_without_nan)