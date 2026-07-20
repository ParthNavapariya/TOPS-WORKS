# Create a Zomato order bill calculator that uses math.floor() to show the final bill amount after applying a 10% discount, rounding down to the nearest rupee.
import math
price = 100
discount = 10
discount_amount = price * discount / 100
final_price = price - discount_amount
print(math.floor(final_price))

