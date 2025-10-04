import pandas as pd
"""
Pandas Series is one of the primary data structures, provides a convenient 
way to handle and manipulate one-dimensional data. It looks similar to 
a single column in a spreadsheet or a single column in a database table.

Series object attributes are tools that help you get information about
series object and its data. Pandas provides multiple attributes to understand 
and manipulate the data in a Series. In this tutorial you will learn about 
Pandas Series attributes.

Data Information
These attributes provide information about the data in the Series −

Sr.No.	Methods & Description
1	
dtype

Returns the data type of the underlying data.

2	
dtypes

Returns the data type of the underlying data.

3	
nbytes

Returns the number of bytes in the underlying data.

4	
ndim

Returns the number of dimensions of the underlying data, which is always 1 for a Series.

5	
shape

Returns a tuple representing the shape of the underlying data.

6	
size

Returns the number of elements in the underlying data.

7	
values

Returns the Series as an ndarray or ndarray-like object depending on the 
data type.

Data Access
These attributes help in accessing data within the Series −

Sr.No.	Methods & Description
1	
at

Accesses a single value using a row/column label pair.

2	
iat

Accesses a single value by integer position.

3	
loc

Accesses a group of rows and columns by labels or a boolean array.

Data Properties
These attributes provide properties and metadata about the Series −

Sr.No.	Methods & Description
1	
empty

Indicates whether the Series or DataFrame is empty.

2	
flags

Gets the properties associated with the Pandas object.

3	
hasnans

Returns True if there are any NaN values.

4	
index

Returns the index (axis labels) of the Series.

5	
is_monotonic_decreasing

Returns True if the values are monotonically decreasing.

6	
is_monotonic_increasing

Returns True if the values are monotonically increasing.

7	
is_unique

Returns True if all values are unique.

8	
name

Returns the name of the Series.

Other
This category includes attributes that perform a variety of other operations −

Sr.No.	Methods & Description
1	
array

Provides the underlying data of the Series as an ExtensionArray.

2	
attrs

Returns a dictionary of global attributes of the dataset.

3	
axes

Returns a list of the row axis labels.

4	
T

Returns the transpose of the Series, which is essentially the same as the original Series.
"""