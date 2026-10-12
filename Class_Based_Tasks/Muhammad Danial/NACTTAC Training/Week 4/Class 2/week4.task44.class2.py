# PDF class alignment: Supervised learning and regression
# Topics: Regression/classification, labeled data, hypothesis, cost function, optimizer.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 44: Pandas DataFrame
# Source/topic: https://www.w3schools.com/python/pandas_dataframes.asp

# Task 44 — Pandas DataFrame
import pandas as pd
df = pd.DataFrame({
    "name": ["Ali", "Sara", "Zain"],
    "age": [20, 21, 19],
    "score": [78, 91, 84]
})
print(df)
print(df[["name", "score"]])
print(df.loc[df["score"] >= 85])
