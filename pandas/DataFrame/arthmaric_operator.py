"""
Addition	df + 2	Adds 2 to each element of the DataFrame
Subtraction	df - 2	Subtracts 2 from each element
Multiplication	df * 2	Multiplies each element by 2
Division	df / 2	Divides each element by 2
Exponentiation	df ** 2	Raises each element to the power of 2
Modulus	df % 2	Finds the remainder when divided by 2
Floor Division	df // 2	Divides and floors the quotient
"""
import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# Display the input DataFrame
print("Input DataFrame:\n", df)

# Perform arithmetic operations
print("\nAddition:\n", df + 2)
print("\nSubtraction:\n", df - 2)
print("\nMultiplication:\n", df * 2)
print("\nDivision:\n", df / 2)
print("\nExponentiation:\n", df ** 2)
print("\nModulus:\n", df % 2)
print("\nFloor Division:\n", df // 2)

# Create two DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
df2 = pd.DataFrame({'A': [10, 20, 30], 'B': [50, 60, 70]}, index=[1, 2, 3])

# Display the input DataFrames
print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)

# Perform arithmetic operations
print("\nAddition of Two DataFrames:\n", df1 + df2)
print("\nSubtraction of Two DataFrames:\n", df1 - df2)
print("\nMultiplication of Two DataFrames:\n", df1 * df2)
print("\nDivision of Two DataFrames:\n", df1 / df2)