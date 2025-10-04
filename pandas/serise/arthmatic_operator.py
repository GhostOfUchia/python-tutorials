import pandas as pd

s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

# Display the Input Series
print('Input Series\n',s)

# Apply all Arithmetic Operation and Display the Results
print('\nAddition:\n',s+2)
print('\nSubtraction:\n', s-2)
print('\nMultiplication:\n', s * 2)
print('\nDivision:\n', s/2)
print('\nExponentiation:\n', s**2)
print('\nModulus:\n', s%2)
print('\nFloor Division:\n', s//2)


# Arithmetic Operations Between Two Series
s1 = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
s2 = pd.Series([9, 8, 6, 5], index=['a','b','c','d'])

# Apply all Arithmetic Operations and Display the Results
print('\nAddition:\n',s1+s2)
print('\nSubtraction:\n', s1-s2)
print('\nMultiplication:\n', s1 * s2)
print('\nDivision:\n', s1/s2)