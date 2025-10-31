import pandas as pd
import numpy as np


# Example: Reindexing a Series

s = pd.Series(np.random.randint(5), index=["a", "b", "c", "d", "e"])
print("Original Series:\n",s)

s_reindexed = s.reindex(["e", "b", "f", "d"])
print('\nOutput Reindexed Series:\n',s_reindexed)


#  Example: Reindexing a DataFrame
N=5

df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
})

print("Original DataFrame:\n", df)

#reindex the DataFrame
df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])

print("\nOutput Reindexed DataFrame:\n",df_reindexed)



# Reindex to Align with Other Objects

df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])

df1 = df1.reindex_like(df2)
print(df1)

# Padding NaNs
print(df2.reindex_like(df1))

# Now fill the NaNs with preceding values
print("Data Frame with Forward Fill:")
print(df2.reindex_like(df1, method='ffill'))


# Padding NaNs
print(df2.reindex_like(df1))

# Now fill the NaNs with preceding values
print("Data Frame with Forward Fill limiting to 1:")
print(df2.reindex_like(df1, method='ffill', limit=1))