import pandas as pd

# Create a Pandas Series
s = pd.Series([1, 2, 3])

# Convert Series to a Python list
result = s.to_list()

print("Output:",result)
print("Output Type:", type(result))

# convert serise to a numpy array
# Convert Series to a NumPy Array
result1 = s.to_numpy()

print("Output:",result1)
print("Output Type:", type(result1))

# Convert Series to a Python dictionary
result3 = s.to_dict()

print("Output:",result3)
print("Output Type:", type(result3))

# Convert Series to a Pandas DataFrame
result4 = s.to_frame(name='Numbers')

print("Output:\n",result4)
print("Output Type:", type(result4))

# Convert Series to string representation
result5 = s.to_string()

print("Output:",repr(result5))
print("Output Type:", type(result5))