# Given a list of food item prices from a Zomato order: [120, 250, 99, 180, 310], use a lambda function with the map() function to add a 10% service charge to each price and print the updated list.

Zomato_order = [120,250,99,180,310]
final = lambda i:i + i*10/100
resuly = list(map(final,Zomato_order))
print(resuly)
