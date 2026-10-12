# PDF class alignment: Python data structures
# Topics: Lists, tuples, dictionaries and sets.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 9: Quadratic equation (image example)
# Source/topic: NAVTTC PDF task image

# Task 9 — Solve ax² + bx + c = 0, including complex roots
import cmath
a, b, c = 1, 5, 6
if a == 0:
    print("This is not a quadratic equation because a must not be zero.")
else:
    discriminant = b*b - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    print("Solutions:", root1, "and", root2)
