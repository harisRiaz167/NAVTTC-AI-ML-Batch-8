# PDF class alignment: NumPy foundations
# Topics: Create arrays from lists/built-ins/random, array attributes, reshape, max/min, argmax/argmin, copy, append, insert, sort, delete, concatenate and split.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 37: NumPy splitting arrays
# Source/topic: https://www.w3schools.com/python/numpy_array_split.asp

# Task 37 — Split NumPy arrays
import numpy as np
arr = np.arange(12)
print("Equal split:", np.split(arr, 3))
matrix = np.arange(16).reshape(4, 4)
print("Split by rows:", np.vsplit(matrix, 2))
