# PDF class alignment: Functions and file handling
# Topics: Functions, scope, lambda, map/filter, nested functions, file handling and exception handling.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 26: Exception handling
# Source/topic: https://www.programiz.com/python-programming/exception-handling

# Task 26 — Exception handling
try:
    numerator = float(input("Numerator: "))
    denominator = float(input("Denominator: "))
    result = numerator / denominator
except ValueError:
    print("Please enter numeric values.")
except ZeroDivisionError:
    print("The denominator cannot be zero.")
else:
    print("Result:", result)
finally:
    print("Calculation finished.")
