# Given two lists — one of product names and one of their prices — use the zip() function to create a dictionary mapping each product to its price, then print the dictionary.

product = ["mobile","headphone","laptop"]
price = [100000,10000,150000]
final = dict(zip(product,price))
print(final)