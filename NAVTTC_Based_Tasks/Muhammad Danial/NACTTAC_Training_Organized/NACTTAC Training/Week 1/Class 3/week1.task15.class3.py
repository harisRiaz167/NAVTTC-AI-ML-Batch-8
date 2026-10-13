# PDF class alignment: Conditions and loops
# Topics: if/elif/else, nested conditions, ternary expressions, break/continue/pass, while/for, enumerate, nested loops, comprehensions, iterators/iterables.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 15: For loops
# Source/topic: https://www.geeksforgeeks.org/python-for-loops/

# Task 15 — For loops (GeeksforGeeks exercise)
for number in range(1, 6):
    print(number)

names = ["Ali", "Sara", "Muneeb"]
for index, name in enumerate(names, start=1):
    print(index, name)

# Iterate over a string
for character in "Python":
    print(character)
