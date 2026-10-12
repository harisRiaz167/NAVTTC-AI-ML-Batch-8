# PDF class alignment: Linear regression with gradient descent
# Topics: Univariate linear regression without vectorization and with vectorization.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 45: Read CSV with Pandas
# Source/topic: https://www.w3schools.com/python/pandas_csv.asp

# Task 45 — Open a CSV file with Pandas
import pandas as pd
from pathlib import Path
path = Path("sample.csv")
if path.exists():
    df = pd.read_csv(path)
    print(df.head())
    print(df.info())
else:
    # Example dataset so the file runs without an external CSV.
    df = pd.DataFrame({"name": ["Ali", "Sara"], "score": [80, 92]})
    df.to_csv(path, index=False)
    print(f"Created example file: {path.resolve()}")
    print(df)
