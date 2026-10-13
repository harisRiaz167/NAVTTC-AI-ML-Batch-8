# PDF class alignment: Pandas advanced operations
# Topics: Merge/join/concatenate, GroupBy, discretization/binning and saving data.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 46: Pandas data analysis
# Source/topic: https://www.w3schools.com/python/pandas_analyzing.asp

# Task 46 — Pandas data analysis
import pandas as pd
df = pd.DataFrame({"team": ["A", "A", "B", "B"], "sales": [100, 120, 90, 150]})
print(df.describe())
print("Mean sales:", df["sales"].mean())
print("Sales by team:\n", df.groupby("team")["sales"].sum())
