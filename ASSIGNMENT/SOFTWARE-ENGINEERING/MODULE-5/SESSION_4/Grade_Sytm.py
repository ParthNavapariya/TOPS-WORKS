# Build a Python script that asks the user for their marks (0-100) and prints their grade based on this rule: 90+ = 'A', 75-89 = 'B', 60-74 = 'C', 40-59 = 'D', below 40 = 'F'. Use if, elif, and else.

marks = int(input("Enter Your Marks 0-100"))

if marks >= 90:
    print("'A'")
elif marks >= 75 and marks <= 89:
    print("'B'")
elif marks >= 60 and marks <= 74:
    print("'c'")
elif marks >= 40 and marks <= 59:
    print("'D'")
else :
    print("'F'")