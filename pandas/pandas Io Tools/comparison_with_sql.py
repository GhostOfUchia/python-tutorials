import pandas as pd

url = 'https://raw.githubusercontent.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/tips.csv'

tips=pd.read_csv(url)
print(tips.head())


# SELECT total_bill, tip, smoker, time
# FROM tips
# LIMIT 5;
print(tips[['total_bill', 'tip', 'smoker', 'time']].head(3))

# SELECT * FROM tips WHERE time = 'Dinner' LIMIT 5; in SQL queary
print(tips[tips['time'] == 'Dinner'].head(5))

# SELECT sex, count(*)
# FROM tips
# GROUP BY sex;

print(tips.groupby('sex').size())

# SELECT * FROM tips
# LIMIT 5 ;
print(tips.head(2))

tips = tips[['smoker', 'day', 'time']].head(5)
print(tips)