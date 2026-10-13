# PDF class alignment: Descriptive statistics
# Topics: Mean, median, mode, variance, standard deviation, coefficient of variation, skewness, kurtosis, z-score, percentile and quartile.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 50: Standard deviation
# Source/topic: https://www.w3schools.com/python/python_ml_standard_deviation.asp

# Task 50 — Standard deviation
from statistics import pstdev, stdev
values = [2, 4, 4, 6, 8]
print("Population standard deviation:", pstdev(values))
print("Sample standard deviation:", stdev(values))
