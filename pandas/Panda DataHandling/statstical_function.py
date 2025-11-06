import pandas as pd
import numpy as np
s = pd.Series([1,2,3,4,5,4])
print(s)
print(s.pct_change)

df = pd.DataFrame(np.random.randint(1,10,size=(4,3)))
print(df)
print(df.pct_change())

"""
🔹 What is Covariance?

Covariance tells us how two variables change together.

If both increase or decrease together, covariance is positive.

If one increases while the other decreases, covariance is negative.

If there is no consistent pattern, covariance is close to zero.

🔹 Simple Example:

Imagine you are studying two things:

📈 Hours studied

🧠 Exam score

If students who study more hours usually get higher scores,
then both values move in the same direction → positive covariance.

If students who study more hours somehow get lower scores (weird, but possible 😅),
then they move in opposite directions → negative covariance.

If there is no clear link, covariance will be near zero.



It basically measures how far each pair of values 
is from their respective means.

🔹 In short:
Covariance Value	Meaning
Positive (+)	Variables move in same direction
Negative (−)	Variables move in opposite direction
Zero (0)	No relationship between them
"""
# Create some simple data
data = {
    'Study_Hours': [2, 4, 6, 8, 10],
   # 'Exam_Score':  [50, 55, 65, 70, 80]  # positive number covariance
   'Exam_Score': [80, 70, 60, 50, 40]  # negative number covariance
}

df = pd.DataFrame(data)

# Calculate covariance
covariance = df['Study_Hours'].cov(df['Exam_Score'])

print("Covariance between Study Hours and Exam Score:", covariance)

"""
🔹 What is Correlation?

Correlation tells us how strongly two variables are related — 
and in what direction.

It is like a standardized version of covariance (easier to interpret).

Correlation Value	Meaning
+1	               Perfect positive relationship (both increase together)
-1	               Perfect negative relationship (one increases, the other decreases)
0	               No relationship
"""


# Sample data
data2 = {
    'Study_Hours': [2, 4, 6, 8, 10],
    'Exam_Score':  [50, 55, 65, 70, 80]
}

df2 = pd.DataFrame(data)

# Calculate correlation
correlation = df2['Study_Hours'].corr(df2['Exam_Score'])

print("Correlation between Study Hours and Exam Score:", correlation)

"""
What does "Ranking" mean?

Ranking means giving a position (rank) to each value —
like 1st, 2nd, 3rd, … — based on its size (highest or lowest).

Example:
If you have marks [80, 90, 70],
their ranks are → [2, 1, 3] (because 90 is highest → rank 1).
"""

# Example data
rankData = {'Marks': [80, 90, 70, 90]}
rank_df = pd.DataFrame(rankData)

# Rank the data
rank_df['Rank'] = rank_df['Marks'].rank(ascending=False)

print(rank_df)