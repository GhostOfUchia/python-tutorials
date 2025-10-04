import numpy as np
data = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])

# Calculating the maximum value
max_value = np.max(data)

print("Maximum value:", max_value)

# Create a 2D array
data_2d = np.array([[1, 3, 5], [2, 4, 6], [7, 8, 9]])

# Calculate the maximum value along axis 0 (columns)
max_axis_0 = np.max(data_2d, axis=0)

# Calculate the maximum value along axis 1 (rows)
max_axis_1 = np.max(data_2d, axis=1)

print("Maximum value along axis 0:", max_axis_0)
print("Maximum value along axis 1:", max_axis_1)

# Create a 3D array
data_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Maximum value along axis 0
max_3d_axis_0 = np.max(data_3d, axis=0)

# Maximum value along axis 1
max_3d_axis_1 = np.max(data_3d, axis=1)

# Maximum value along axis 2
max_3d_axis_2 = np.max(data_3d, axis=2)

print("Maximum value along axis 0:", max_3d_axis_0)
print("Maximum value along axis 1:", max_3d_axis_1)
print("Maximum value along axis 2:", max_3d_axis_2)

# Create an array with NaN values
data_with_nan = np.array([1, 3, np.nan, 5, 7])

# Calculate the maximum value while ignoring NaN values
max_without_nan = np.nanmax(data_with_nan)

print("Maximum value without NaN:", max_without_nan)

# Create an array
data = np.array([5, 2, 9, 1, 5, 6])

# Create an output array
out_array = np.empty((), dtype=np.int32)

# Calculate the maximum value and store it in out_array
np.max(data, out=out_array)

print("Output array:", out_array)