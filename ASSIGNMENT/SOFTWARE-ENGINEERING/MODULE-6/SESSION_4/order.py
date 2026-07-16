# Convert the tuple order = ('Burger', 'Fries', 'Coke') into a list, add 'Ice Cream' to the end, then convert it back to a tuple and print the final tuple.

order = ('Burger','Fries','Coke')
lst = list(order)

lst.append("Ice Cream")

final = tuple(lst)
print(final)


