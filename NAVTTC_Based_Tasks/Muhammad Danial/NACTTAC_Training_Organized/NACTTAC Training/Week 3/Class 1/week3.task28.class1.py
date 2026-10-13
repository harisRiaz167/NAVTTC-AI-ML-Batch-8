# PDF class alignment: NumPy data operations
# Topics: Loading/saving, indexing, 2D selection, logical selection, broadcasting, casting, arithmetic and universal functions.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 28: NumPy create arrays
# Source/topic: https://www.w3schools.com/python/numpy_creating_arrays.asp

# Task 28 — Create NumPy arrays
import numpy as np
from_list = np.array([1, 2, 3, 4])
zeros = np.zeros((2, 3))
ones = np.ones(4, dtype=int)
sequence = np.arange(0, 10, 2)
random_values = np.random.default_rng(42).random(3)
print(from_list, zeros, ones, sequence, random_values, sep="\n")
