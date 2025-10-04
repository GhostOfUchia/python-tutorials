"""
A Series is a one-dimensional labeled array that can hold any data type. 
It can store integers, strings, floating-point numbers, etc. 
Each value in a Series is associated with a label (index), 
which can be an integer or a string.

"""
import pandas as pd

data1 = [1,2,3,4,5,6,7]
serise1 = pd.Series(data1)

data2 = ["Amit","Gulshna","Ravi"]
serise2 = pd.Series(data2)

data3 = ["Amit",35,"saini",True]
serise3 = pd.Series(data3,index=["Name = ","Age = ","Surname = ","Is Male = "])
print(serise3)