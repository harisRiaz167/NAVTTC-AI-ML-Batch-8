# PDF class alignment: NumPy data operations
# Topics: Loading/saving, indexing, 2D selection, logical selection, broadcasting, casting, arithmetic and universal functions.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 38: NumPy searching
# Source/topic: https://www.w3schools.com/python/numpy_array_search.asp

# Task 38 — Search NumPy arrays
import numpy as np
arr = np.array([5, 8, 2, 8, 10])
print("Positions equal to 8:", np.where(arr == 8)[0])
print("Values greater than 6:", arr[arr > 6])
