# PDF class alignment: Conditions and loops
# Topics: if/elif/else, nested conditions, ternary expressions, break/continue/pass, while/for, enumerate, nested loops, comprehensions, iterators/iterables.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 25: Dictionary data type
# Source/topic: https://www.programiz.com/python-programming/dictionary

# Task 25 — Dictionaries (Programiz exercise)
student = {"name": "Muneeb", "course": "AI/ML", "score": 88}
print(student["name"])
student["score"] = 92
student["city"] = "Bahawalpur"
for key, value in student.items():
    print(f"{key}: {value}")
