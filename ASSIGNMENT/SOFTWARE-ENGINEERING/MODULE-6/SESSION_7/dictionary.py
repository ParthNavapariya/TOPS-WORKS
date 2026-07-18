# This Python script takes a string input from the user and prints a dictionary showing how many times each character appears in the string.

user = input("Enter string")

count = {}
for char in user:
    if char in count:
        count[char]=+1
    else:
        count[char] = 1
print(count)