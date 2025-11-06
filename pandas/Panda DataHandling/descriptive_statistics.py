"""
🔹 What is Descriptive Statistics?

Descriptive statistics means summarizing your data —
showing key information like mean, median, min, max, count, std, etc.
It helps you understand what your data looks like before doing any deep analysis.
"""

import pandas as pd

data = {
    'Marks': [80, 90, 75, 95, 85],
    'Age': [18, 19, 18, 20, 19]
}

df = pd.DataFrame(data)

# Get descriptive statistics
print(df.describe())

print(df.describe(include='object'))  # For categorical data

"""
Output looks like this:
	      Marks	     Age
count	  5.0        5.0
mean	  85.0	     18.8
std    	  7.9	     0.8
min	      75.0	     18.0
25%	      80.0	     8.0
50%	      85.0	     19.0
75%	      90.0	     19.0
max	      95.0	     20.0
🔹 What each part means:
Term	         Meaning
count	         How many values
mean	         Average value
std	             Standard deviation (spread of data)
min / max	     Smallest and largest values
25%, 50%, 75%	 Percentiles (middle points of data)
"""