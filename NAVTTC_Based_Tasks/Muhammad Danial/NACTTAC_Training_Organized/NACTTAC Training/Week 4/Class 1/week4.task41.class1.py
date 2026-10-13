# PDF class alignment: Pandas advanced operations
# Topics: Merge/join/concatenate, GroupBy, discretization/binning and saving data.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 41: Pandas basics
# Source/topic: https://www.w3schools.com/python/pandas_tutorial.asp

# Task 41 — Pandas basics
import pandas as pd
df = pd.DataFrame({"name": ["Ali", "Sara", "Zain"], "score": [78, 91, 84]})
print(df)
print(df.head())
print(df.describe(numeric_only=True))
