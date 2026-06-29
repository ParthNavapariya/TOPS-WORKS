# Create a loop that goes through the following list: ['Pizza', 'Burger', 'Pasta', 'Sandwich', 'Burger King'], and breaks the loop when it finds 'Burger King', printing 'Found Burger King, stopping search.'

lst = ['Pizza', 'Burger', 'Pasta', 'Sandwich', 'Burger King']

for i in lst:
    if i == "Burger King":
     break
    print(i)
print("Found Burger King, stopping search.")