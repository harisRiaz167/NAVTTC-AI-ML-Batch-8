# PDF class alignment: Python data structures
# Topics: Lists, tuples, dictionaries and sets.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 19: Looping techniques
# Source/topic: https://www.geeksforgeeks.org/looping-techniques-python/

# Task 19 — Useful looping techniques
numbers = [10, 20, 30]
names = ["Ali", "Sara", "Zain"]

for i, number in enumerate(numbers):
    print(i, number)

for name, number in zip(names, numbers):
    print(name, number)

for key, value in {"name": "Muneeb", "course": "AI/ML"}.items():
    print(key, value)

for number in reversed(numbers):
    print(number)
