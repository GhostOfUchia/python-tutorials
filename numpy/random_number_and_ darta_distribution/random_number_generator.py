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

np.random.seed(42) # Set the seed
print(np.random.rand(3))

np.random.seed(42) # Set the same seed again
print(np.random.rand(3))