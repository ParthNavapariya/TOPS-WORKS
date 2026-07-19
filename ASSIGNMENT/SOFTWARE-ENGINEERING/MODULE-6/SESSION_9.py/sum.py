# Create a lambda function that takes two numbers and returns their sum and product as a tuple. Use it to process the pairs (3, 4), (5, 2), and (7, 8).<br><br><em><strong>Hint:</strong> You can return multiple values from a lambda by returning a tuple: (a+b, a*b).</em>

sum = lambda a,b: a+b
product = lambda a,b: a*b


final = (sum(3,4),product(3,4))
final2 = (sum(5,2),product(5,2))
final3 = (sum(7,8),product(7,8))
print(final)
print(final2)
print(final3)

