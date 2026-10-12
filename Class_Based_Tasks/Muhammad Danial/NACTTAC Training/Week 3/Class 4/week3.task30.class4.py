# PDF class alignment: Pandas cleaning
# Topics: head, unique, value_counts, custom functions, sorting, null checks, replacements, dropping rows/columns and missing-data handling.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 30: NumPy slicing
# Source/topic: https://www.w3schools.com/python/numpy_array_slicing.asp

# Task 30 — NumPy slicing
import numpy as np
arr = np.arange(10)
print("2 through 6:", arr[2:7])
print("Every second:", arr[::2])
matrix = np.arange(12).reshape(3, 4)
print("First two rows, columns 1-2:\n", matrix[:2, 1:3])
