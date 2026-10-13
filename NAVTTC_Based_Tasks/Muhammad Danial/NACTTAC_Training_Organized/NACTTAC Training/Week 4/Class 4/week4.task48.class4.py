# PDF class alignment: Machine learning overview
# Topics: Types of ML and classical pipeline: collection, preprocessing, feature crafting, modeling, testing/evaluation and deployment.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 48: Pandas correlation
# Source/topic: https://www.w3schools.com/python/pandas_correlations.asp

# Task 48 — Pandas correlation
import pandas as pd
df = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5],
    "score": [50, 55, 65, 70, 80],
    "sleep_hours": [8, 7, 8, 6, 7]
})
print(df.corr(numeric_only=True))
