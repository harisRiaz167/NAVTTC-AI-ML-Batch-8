# PDF class alignment: Testing and evaluation
# Topics: Testing, evaluation metrics, classification/regression and dataset imbalance remedies.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 55: Time series analysis
# Source/topic: https://www.dataquest.io/blog/tutorial-time-series-analysis-with-pandas

# Task 55 — Time-series analysis with Pandas
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.date_range("2025-01-01", periods=60, freq="D")
values = [100 + i * 0.7 + ((i % 7) - 3) * 2 for i in range(len(dates))]
series = pd.Series(values, index=dates, name="value")
print("Daily data:\n", series.head())
print("Weekly mean:\n", series.resample("W").mean())
print("7-day rolling average:\n", series.rolling(7).mean().dropna().head())

series.plot(title="Example time series and 7-day rolling mean", legend=True)
series.rolling(7).mean().plot(label="7-day rolling mean", legend=True)
plt.xlabel("Date")
plt.ylabel("Value")
plt.tight_layout()
plt.show()
