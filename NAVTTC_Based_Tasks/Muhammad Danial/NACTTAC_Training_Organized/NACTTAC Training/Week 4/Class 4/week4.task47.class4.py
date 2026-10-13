# PDF class alignment: Visualization with Pandas and Seaborn
# Topics: Area/bar/density/histogram/line/scatter/box/KDE/pie; distribution, joint, pair, categorical and heatmap plots.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 47: Pandas data cleaning
# Source/topic: https://www.w3schools.com/python/pandas_cleaning.asp

# Task 47 — Pandas data cleaning
import pandas as pd
df = pd.DataFrame({
    "name": ["Ali", "Sara", None, "Ali"],
    "age": [20, None, 22, 20],
    "city": ["Lahore", "Karachi", "Multan", "Lahore"]
})
print("Missing values before:\n", df.isna().sum())
df = df.drop_duplicates()
df["name"] = df["name"].fillna("Unknown")
df["age"] = df["age"].fillna(df["age"].median())
print("Cleaned data:\n", df)
