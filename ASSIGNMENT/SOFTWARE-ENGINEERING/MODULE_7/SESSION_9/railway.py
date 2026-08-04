# Use ChatGPT to generate a regular expression that matches Indian Railways PNR numbers (10-digit numbers), then implement a Python function is_valid_pnr(pnr) using re.match() to validate user input. Paste the regex and your function in your submission.

import re

def is_valid_pnr(pnr):
    pattern = r'^\d{10}$'
    return re.match(pattern, pnr) is not None

# Example
pnr = input("Enter PNR number: ")

if is_valid_pnr(pnr):
    print("Valid PNR")
else:
    print("Invalid PNR")