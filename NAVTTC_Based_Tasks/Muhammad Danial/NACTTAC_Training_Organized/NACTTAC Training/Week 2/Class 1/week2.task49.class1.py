# PDF class alignment: Statistics and data types
# Topics: Structured/unstructured data; quantitative/qualitative; numerical, continuous, discrete, categorical, nominal, ordinal and binary variables.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 49: Mean median mode
# Source/topic: https://www.w3schools.com/python/python_ml_mean_median_mode.asp

# Task 49 — Mean, median, and mode
from statistics import mean, median, multimode
values = [2, 4, 4, 6, 8]
print("Mean:", mean(values))
print("Median:", median(values))
print("Mode(s):", multimode(values))
