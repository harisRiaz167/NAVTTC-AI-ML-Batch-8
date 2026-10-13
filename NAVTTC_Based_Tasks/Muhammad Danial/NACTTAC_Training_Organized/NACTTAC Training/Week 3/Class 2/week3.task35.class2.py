# PDF class alignment: Pandas cleaning
# Topics: head, unique, value_counts, custom functions, sorting, null checks, replacements, dropping rows/columns and missing-data handling.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 35: NumPy iteration
# Source/topic: https://www.w3schools.com/python/numpy_array_iterating.asp

# Task 35 — NumPy array iteration
import numpy as np
arr = np.array([[1, 2], [3, 4]])
for value in np.nditer(arr):
    print(value)
print("Rows:")
for row in arr:
    print(row)
