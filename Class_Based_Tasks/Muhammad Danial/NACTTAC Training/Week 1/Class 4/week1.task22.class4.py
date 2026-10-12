# PDF class alignment: Linux shell fundamentals
# Topics: pwd, cd, ls, cat, man, redirection, mkdir/rm/cp/mv, file reading, touch/nano, bash/sh, chmod, ps/kill, package management, environment variables.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 22: Tuple data type
# Source/topic: https://www.programiz.com/python-programming/tuple

# Task 22 — Tuples (Programiz exercise)
coordinates = (10, 20)
print("x:", coordinates[0], "y:", coordinates[1])
print("Length:", len(coordinates))
# Tuples are immutable; create a new tuple to add an item.
coordinates = coordinates + (30,)
print(coordinates)
