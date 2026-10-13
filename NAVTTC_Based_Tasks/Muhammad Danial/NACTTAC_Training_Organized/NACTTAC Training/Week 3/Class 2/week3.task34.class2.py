# PDF class alignment: Pandas foundations
# Topics: Series, DataFrames, data input, row/column selection, conditional selection and indexing.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 34: NumPy reshape
# Source/topic: https://www.w3schools.com/python/numpy_array_reshape.asp

# Task 34 — NumPy reshaping
import numpy as np
arr = np.arange(12)
matrix = arr.reshape(3, 4)
print(matrix)
print("Flattened:", matrix.reshape(-1))
