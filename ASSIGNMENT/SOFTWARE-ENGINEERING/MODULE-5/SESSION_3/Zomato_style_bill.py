# Build a Zomato-style bill calculator: take the price of a food item and quantity as input, convert them to float and int, calculate the total bill, and display it with a message like 'Your total bill is ₹350.50'.

print("ZOMATO_STYLE_BILL_CALCULATOR")

print("1.pizza = 350 \n 2.Burger = 450 \n 3.Sandwich = 90 \n 4.vadapav = 100")

food = int(input("Enter Food Number"))
quantity = int(input("Enter Food Quantity"))


if food == 1:
       price = float(350)
elif food == 2:
       price = float(450)
elif food == 3:
        price = float(90)
elif food == 4:
        price = float(100)
else : 
        print("invalid Order")
    
totalbill = price * quantity
print(f"You Bill Is {totalbill}")




