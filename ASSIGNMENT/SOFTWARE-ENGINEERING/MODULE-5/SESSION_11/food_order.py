# Given a dictionary called food_order = {'Pizza': 2, 'Burger': 1, 'Fries': 3}, use the keys(), values(), and items() methods to print: a) all food items, b) all quantities, and c) each item with its quantity.

food_order = {
    'pizza' : 2,
    'burger' : 3,
    'frens-fries' : 4,
    'panni' : 5,
    'pasta' : 6
}

print(food_order)
print("a = all food \n b = all quantites \n c =each item with its quantites")
choose = input("enter your choice")
if choose == "a":
        for j in food_order.keys():
            print(j)
elif choose == "b":
    for i in food_order.values():
     print(i)
else :
     for ket,value in food_order.items():
       print(ket,value)
