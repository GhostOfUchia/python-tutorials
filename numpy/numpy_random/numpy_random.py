from numpy import random

# Generate Random Number

x = random.randint(10)   # its generate int

y = random.rand(1)      # its generate float value

# Generate a 1-D array containing 5 random integers from 0 to 100:
# The randint() method takes a size parameter 
# where you can specify the shape of an array.

a = random.randint(100,size = (5))

# Generate a 2-D array with 3 rows, each row containing 5 random 
# integers from 0 to 100:
b = random.randint(10,size = (5,5))

# Generate a 1-D array containing 5 random floats:
# The rand() method also allows you to specify the shape of the array.
c = random.rand(6)

# Generate a 2-D array with 3 rows, each row containing 5 random numbers:
d = random.rand(3,2)

# Generate Random Number From Array
# The choice() method allows you to generate a random 
# value based on an array of values.
# The choice() method takes an array as a parameter
# and randomly returns one of the values.
e = random.choice([1,2,3,4,5])

# The choice() method also allows you to return an array of values.
# Add a size parameter to specify the shape of the array.
f = random.choice([2,3,4,5,6],size=(3,5))
print(f)
