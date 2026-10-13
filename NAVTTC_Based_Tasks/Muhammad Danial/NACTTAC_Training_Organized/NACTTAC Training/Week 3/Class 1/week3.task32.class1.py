# PDF class alignment: NumPy foundations
# Topics: Create arrays from lists/built-ins/random, array attributes, reshape, max/min, argmax/argmin, copy, append, insert, sort, delete, concatenate and split.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 32: NumPy copy vs view
# Source/topic: https://www.w3schools.com/python/numpy_copy_vs_view.asp

# Task 32 — NumPy copying and viewing
import numpy as np
original = np.array([1, 2, 3])
copied = original.copy()
viewed = original.view()
original[0] = 99
print("Original:", original)
print("Copy (independent):", copied)
print("View (shares underlying data):", viewed)
print("Shares memory:", np.shares_memory(original, viewed))
