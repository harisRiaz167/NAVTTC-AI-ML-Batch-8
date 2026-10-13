# PDF class alignment: Introduction, course orientation and software setup
# Topics: AI overview, job market, applications, work ethics, career opportunities; install Python/Anaconda/VS Code/PyCharm.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 6: Square root of real or complex number (image example)
# Source/topic: NAVTTC PDF task image

# Task 6 — Square root of a real or complex number
import cmath
num = 1 + 2j
root = cmath.sqrt(num)
print(f"The square root of {num} is {root.real:.3f} + {root.imag:.3f}j")
