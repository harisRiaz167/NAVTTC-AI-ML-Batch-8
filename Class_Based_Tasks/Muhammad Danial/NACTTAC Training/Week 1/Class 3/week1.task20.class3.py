# PDF class alignment: Descriptive statistics
# Topics: Mean, median, mode, variance, standard deviation, coefficient of variation, skewness, kurtosis, z-score, percentile and quartile.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 20: User-defined functions
# Source/topic: https://www.geeksforgeeks.org/functions-in-python/

# Task 20 — User-defined functions
def calculate_average(values):
    """Return the arithmetic mean of a non-empty sequence."""
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)

scores = [78, 85, 91]
print("Average:", calculate_average(scores))
