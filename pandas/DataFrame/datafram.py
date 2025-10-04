import pandas as pd

df = pd.DataFrame()
print(df)

# create a dataframe from a list
data = [1,2,3,4,5]
dfram = pd.DataFrame(data)
print(dfram)

# creat dataframe with list of list
data = [['Alex',10],['Bob',12],['Clarke',13]]
dframe = pd.DataFrame(data,columns=['Name','Age'],index=[1,2,3])
print(dframe)

# Create a DataFrame from Dict of ndarrays / Lists
dictdata = { 'Name':['Amit','Gulshan','Ravi'],'Age':[32,34,35]}
dictdframe = pd.DataFrame(dictdata)
print(dictdframe)

# print  with index values
withindex = pd.DataFrame(dictdata,index=[1,2,3])
print(withindex)

# Create a DataFrame from List of Dicts
datalist = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
listofdict = pd.DataFrame(datalist)
print(listofdict)

# create a dataframe with list of serise
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

list_of_serise = pd.DataFrame(d)
print(list_of_serise)