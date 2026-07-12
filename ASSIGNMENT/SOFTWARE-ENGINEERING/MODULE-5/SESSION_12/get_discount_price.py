# Define a function called get_discounted_price that takes price and discount_percent as arguments and returns the final price after applying the discount. Test it with a price of 500 and a discount of 10%.


def get_discounted_price(price,discount):
        totalprice = price - (price*discount/100)
        return totalprice


final = get_discounted_price(500,10)
print(final)