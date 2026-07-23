# Simulate a Flipkart order summary calculator that takes price and quantity as input and calculates the total. Use try-except to handle ValueError if the user enters a non-numeric value, and display an error message.



try: 
    Product_price = int(input("Enter price :"))
    Product_quantity = int(input("Enter qunatity:"))
    Total_amount = Product_price*Product_quantity
    print(Total_amount)
except ValueError:
    print("you have enter number")
