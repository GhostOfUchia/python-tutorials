from numpy import random
import numpy as np
"""
Random Permutations of Elements
A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.

The NumPy Random module provides two methods for this: shuffle() and permutation().
"""

# Shuffle means changing arrangement of elements in-place. i.e. in the array itself.
# The shuffle() method makes changes to the original array.
# Randomly shuffle elements of following array:
a = np.array([1,2,3,4,5])
random.shuffle(a)

# Generate a random permutation of elements of following array:
b = np.array([1,2,3,4,5])
c = random.permutation(b) 
# The permutation() method returns a re-arranged array (and leaves the original array un-changed).
print(c)