import numpy as np

# Define an array
array = np.array([1, 2, 3, 4, 5])

# Shuffle the array in place
np.random.shuffle(array)
print("Shuffled array:", array)

# Generate a permutation of the array
permuted_array = np.random.permutation(array)
print("Original array:", array)
print("Permuted array:", permuted_array)

# Define a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Shuffle the array in place
np.random.shuffle(array_2d)
print("Shuffled 2D array:", array_2d)

# Generate a permutation of the 2D array
permuted_array_2d = np.random.permutation(array_2d)
print("Original 2D array:", array_2d)
print("Permuted 2D array:", permuted_array_2d)

# Generate a random permutation of integers from 0 to 9
random_permutation = np.random.permutation(10)
print("Random permutation of integers from 0 to 9:", random_permutation)

# Set the seed for reproducibility
np.random.seed(42)

# Define an array
array = np.array([1, 2, 3, 4, 5])

# Shuffle the array in place
np.random.shuffle(array)
print("Shuffled array with seed 42:", array)

# Reset the seed and shuffle again to get the same result
np.random.seed(42)
np.random.shuffle(array)
print("Shuffled array with seed 42 (again):", array)

# Define a dataset
dataset = np.array([[1, 'A'], [2, 'B'], [3, 'C'], [4, 'D'], [5, 'E']])

# Shuffle the dataset in place
np.random.shuffle(dataset)
print("Shuffled dataset:", dataset)

# Split the dataset into training and testing sets
train_set = dataset[:3]
test_set = dataset[3:]
print("Training set:", train_set)
print("Testing set:", test_set)