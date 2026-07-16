# You have two lists: one with Zomato restaurant names ['Burger Hub', 'Pizza Point', 'Sushi House'] and another with their delivery times in minutes [30, 25, 40]. Use the zip() function to pair each restaurant with its delivery time and print each pair in the format: 'Burger Hub - 30 min'.

Zomato_restaurant_names = ['Burger Hub', 'Pizza Point', 'Sushi House']
minutes  = ["30min", "25min", "40min"]

final = zip(Zomato_restaurant_names,minutes)

for Zomato_restaurant_names , minutes in final:
    print(Zomato_restaurant_names,"-",minutes)


