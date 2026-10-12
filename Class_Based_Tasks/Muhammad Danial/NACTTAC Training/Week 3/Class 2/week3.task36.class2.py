# PDF class alignment: Statistics, correlation and probability
# Topics: Correlation coefficient, univariate/bivariate/multivariate plots, probability, joint/marginal/conditional probability, distributions and Bayesian probability.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 36: NumPy joining arrays
# Source/topic: https://www.w3schools.com/python/numpy_array_join.asp

# Task 36 — Join NumPy arrays
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Concatenate:", np.concatenate((a, b)))
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
print("Vertical stack:\n", np.vstack((x, y)))
