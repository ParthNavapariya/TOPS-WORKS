# Simulate a Zomato-style order history: create a file orders.txt with at least 5 lines (each line is an order). Write a script that reads and prints each order line-by-line using a loop, and after reading each line, prints the file pointer's position using tell().


with open("order.txt","w") as f:
   f.write("panni\n")
   f.write("burger\n")
   f.write("sandwich\n")
   f.write("puff")


with open("order.txt","r") as f:

    while True:

        order = f.readline()

        if order == "":
            break

        print(order.strip())
        print("File Pointer Position:", f.tell())