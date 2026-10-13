# PDF class alignment: Classes and objects
# Topics: Instance/class variables, methods, constructors/destructors, inheritance types, MRO, access conventions, name mangling, nested classes, association/aggregation/composition.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 27: User-defined exception
# Source/topic: https://www.programiz.com/python-programming/user-defined-exception

# Task 27 — User-defined exception
class InvalidAgeError(Exception):
    """Raised when an age is outside the allowed range."""

def validate_age(age):
    if not 0 <= age <= 120:
        raise InvalidAgeError("Age must be between 0 and 120.")
    return age

try:
    age = int(input("Enter age: "))
    print("Valid age:", validate_age(age))
except ValueError:
    print("Enter a whole number.")
except InvalidAgeError as error:
    print(error)
