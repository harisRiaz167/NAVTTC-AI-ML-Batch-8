# PDF class alignment: Statistics, correlation and probability
# Topics: Correlation coefficient, univariate/bivariate/multivariate plots, probability, joint/marginal/conditional probability, distributions and Bayesian probability.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 31: NumPy data types
# Source/topic: https://www.w3schools.com/python/numpy_data_types.asp

# Task 31 — NumPy data types
import numpy as np
integers = np.array([1, 2, 3], dtype=np.int32)
decimals = np.array([1, 2, 3], dtype=np.float64)
print(integers, integers.dtype)
print(decimals, decimals.dtype)
print("Cast to float:", integers.astype(float))
