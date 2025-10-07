"""
NumPy Random Generator
The random generator in NumPy is used to generate random numbers and 
perform random sampling.

The random module in NumPy offers a wide range of random number 
generation functions, from generating random integers and floating-point 
numbers to more complex distributions like normal, uniform, and binomial 
distributions.

How Does NumPy's Random Generator Work?
The NumPy random number generator is built on top of a pseudorandom number
generator (PRNG) algorithm called the Mersenne Twister. 
The key feature of a PRNG is that it generates a sequence of numbers 
that approximates true randomness, but it is determined by an initial value, 
called a seed.

By setting the same seed, you can ensure that the sequence of 
random numbers is the same every time you run your code, which is 
important for reproducibility in scientific experiments.
"""
import numpy as np
"""
# Set the seed for reproducibility
np.random.seed(1)

# Generate random numbers
random_numbers_1 = np.random.random(5)

# Generate the same random numbers with the same seed
np.random.seed(42)
random_numbers_2 = np.random.random(5)

# Display the result 
print("First random numbers:", random_numbers_1)
print("Second random numbers:", random_numbers_2)

import numpy as np

np.random.seed(24) # Set the seed
print(np.random.rand(3))

np.random.seed(42) # Set the same seed again
print(np.random.rand(3))

"""

# Generate 5 random float numbers between 0 and 1
random_floats = np.random.random(5)
print("Random float numbers:", random_floats)

# Generate 5 random integers between 10 (inclusive) and 100 (exclusive)
random_integers = np.random.randint(10, 100, size=5)
print("Random integers:", random_integers)

# Generate 5 random numbers from a normal distribution with mean=0 and std=1
random_normal = np.random.normal(0, 1, 5)
print("Random numbers from normal distribution:", random_normal)

# Generate 5 random numbers between 1.0 and 10.0
random_uniform = np.random.uniform(1.0, 10.0, 5)
print("Random numbers from uniform distribution:", random_uniform)

# Define an array of elements
array = np.array([1, 2, 3, 4, 5])

# Randomly select 3 elements from the array with replacement
sample_with_replacement = np.random.choice(array, 3, replace=True)
print("Random sample with replacement:", sample_with_replacement)

# Shuffle the array in place
np.random.shuffle(array)
print("Shuffled array:", array)

# create a random generator
rng = np.random.default_rng()

# generate random numbers using the random generator
print(rng.random()) # print one random number between 1 and 0

print(rng.random(5)) # print 1d array of 5 random numbers

print(rng.random((2,3)))# print 2d array of random numbers with 2 rows and 3 columns

# GenerateRandom Integers
print(rng.integers(10, 100)) # print one random integer between 10 and 100

print(rng.integers(10, 100, size=5)) # print 1d array of 5 random integers between 10 and 100

print(rng.integers(10, 100, size=(2,3))) # print 2d array of random integers with 2 rows and 3 columns

# From Normal Distribution
print(rng.normal(0, 1)) # print one random number from normal distribution with mean=0 and std=1

print(rng.normal(0, 1, size=5)) # print 1d array of 5 random numbers from normal distribution with mean=0 and std=1

print(rng.normal(0, 1, size=(2,3))) # print 2d array of random numbers from normal distribution with 2 rows and 3 columns

# Random Choice from a list
print(rng.choice([1, 2, 3, 4, 5])) # print one random element from the list

print(rng.choice([1, 2, 3, 4, 5], size=3, replace=False)) # print 1d array of 3 random elements from the list with replacement

# shuffle an array
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print("Shuffled array using random generator:", array)

# set a seed for reproducibility
rng = np.random.default_rng(seed=42)
print(rng.random(3)) # print 1d array of 3 random numbers