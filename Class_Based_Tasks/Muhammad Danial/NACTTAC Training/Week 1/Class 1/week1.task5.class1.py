# PDF class alignment: Conditions and loops
# Topics: if/elif/else, nested conditions, ternary expressions, break/continue/pass, while/for, enumerate, nested loops, comprehensions, iterators/iterables.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 5: Square root (image example)
# Source/topic: NAVTTC PDF task image

# Task 5 — Calculate square root of a non-negative number
import math
num = float(input("Enter a non-negative number: "))
if num < 0:
    print("Please enter a non-negative number.")
else:
    print(f"The square root of {num} is {math.sqrt(num):.3f}")
