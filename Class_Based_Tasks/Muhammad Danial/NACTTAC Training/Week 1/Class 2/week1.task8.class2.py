# PDF class alignment: Python values and strings
# Topics: Numbers, Booleans, strings, expressions, operators, variables, keywords, string operations, input, type casting and comments.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 8: Area of triangle (image example)
# Source/topic: NAVTTC PDF task image

# Task 8 — Area of a triangle using Heron's formula
import math
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
if min(a, b, c) <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("These sides do not form a valid triangle.")
else:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(f"Area of the triangle = {area:.2f}")
