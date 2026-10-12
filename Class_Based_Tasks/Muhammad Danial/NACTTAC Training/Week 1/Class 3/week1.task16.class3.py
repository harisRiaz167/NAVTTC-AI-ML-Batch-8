# PDF class alignment: Introduction, course orientation and software setup
# Topics: AI overview, job market, applications, work ethics, career opportunities; install Python/Anaconda/VS Code/PyCharm.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 16: While loops
# Source/topic: https://www.geeksforgeeks.org/python-while-loops/

# Task 16 — While loops (GeeksforGeeks exercise)
count = 1
while count <= 5:
    print(count)
    count += 1

# Input loop with a clear stopping condition
while True:
    answer = input("Type q to quit: ").strip().lower()
    if answer == "q":
        break
