import numpy as np
data = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])

# Calculating the minimum value
min_value = np.min(data)

print("Minimum value:", min_value)

# Create a 2D array
data_2d = np.array([[1, 3, 5], [2, 4, 6], [7, 8, 9]])

# Calculate the minimum value along axis 0 (columns)
min_axis_0 = np.min(data_2d, axis=0)

# Calculate the minimum value along axis 1 (rows)
min_axis_1 = np.min(data_2d, axis=1)

print("Minimum value along axis 0:", min_axis_0)
print("Minimum value along axis 1:", min_axis_1)

# Create a 3D array
data_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Minimum value along axis 0
min_3d_axis_0 = np.min(data_3d, axis=0)

# Minimum value along axis 1
min_3d_axis_1 = np.min(data_3d, axis=1)

# Minimum value along axis 2
min_3d_axis_2 = np.min(data_3d, axis=2)

print("Minimum value along axis 0:", min_3d_axis_0)
print("Minimum value along axis 1:", min_3d_axis_1)
print("Minimum value along axis 2:", min_3d_axis_2)

# Create an array with NaN values
data_with_nan = np.array([1, 3, np.nan, 5, 7])

# Calculate the minimum value while ignoring NaN values
min_without_nan = np.nanmin(data_with_nan)

print("Minimum value without NaN:", min_without_nan)

# Create an array
data = np.array([5, 2, 9, 1, 5, 6])

# Create an output array
out_array = np.empty((), dtype=np.int32)

# Calculate the minimum value and store it in out_array
np.min(data, out=out_array)

print("Output array:", out_array)