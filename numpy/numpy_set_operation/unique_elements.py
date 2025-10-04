import numpy as np
# Create a one-dimensional array
data = np.array([1, 2, 2, 3, 4, 4, 4, 5])

# Find unique elements
unique_elements = np.unique(data)

print("Unique elements:", unique_elements)

# Create an array
data = np.array([1, 2, 2, 3, 4, 4, 4, 5])

# Find unique elements and their indices
unique_elements, indices = np.unique(data, return_index=True)

print("Unique elements:", unique_elements)
print("Indices of first occurrences:", indices)


# Create an array
data = np.array([1, 2, 2, 3, 4, 4, 4, 5])

# Find unique elements and inverse indices
unique_elements, inverse_indices = np.unique(data, return_inverse=True)

print("Unique elements:", unique_elements)
print("Inverse indices:", inverse_indices)

# Create an array
data = np.array([1, 2, 2, 3, 4, 4, 4, 5])

# Find unique elements and their counts
unique_elements, counts = np.unique(data, return_counts=True)

print("Unique elements:", unique_elements)
print("Counts of unique elements:", counts)

# Create a 2D array
data_2d = np.array([[1, 2, 2], [3, 4, 4], [4, 5, 5]])

# Find unique elements
unique_elements = np.unique(data_2d)

print("Unique elements:", unique_elements)



# Create a structured array
data_structured = np.array([(1, 'a'), (2, 'b'), (2, 'b'), (3, 'c')],
                           dtype=[('num', 'i4'), ('char', 'U1')])

# Find unique elements considering all fields
unique_elements_structured = np.unique(data_structured)

print("Unique elements in structured array:", unique_elements_structured)