# PDF class alignment: Machine learning overview
# Topics: Types of ML and classical pipeline: collection, preprocessing, feature crafting, modeling, testing/evaluation and deployment.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 43: Pandas Series
# Source/topic: https://www.w3schools.com/python/pandas_series.asp

# Task 43 — Pandas Series
import pandas as pd
scores = pd.Series([78, 91, 84], index=["Ali", "Sara", "Zain"])
print(scores)
print("Sara:", scores["Sara"])
print("Mean:", scores.mean())
