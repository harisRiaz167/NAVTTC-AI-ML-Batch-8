# PDF class alignment: Pandas cleaning
# Topics: head, unique, value_counts, custom functions, sorting, null checks, replacements, dropping rows/columns and missing-data handling.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 40: NumPy random
# Source/topic: https://www.w3schools.com/python/numpy_random.asp

# Task 40 — NumPy random techniques
import numpy as np
rng = np.random.default_rng(42)
print("Random floats:", rng.random(3))
print("Random integers:", rng.integers(1, 7, size=5))
print("Choice:", rng.choice(["red", "green", "blue"], size=4))
