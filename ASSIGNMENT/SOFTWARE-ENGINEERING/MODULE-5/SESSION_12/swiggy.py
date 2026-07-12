# Using reduce() and a lambda function, calculate the total bill amount for a Swiggy order given a list of item prices: [120, 80, 150, 60].<br><br><em><strong>Hint:</strong> Import reduce from functools.</em>

from functools import reduce


swiggy = [120, 80, 150, 60]
total = reduce(lambda x,y:x+y,swiggy)
print(total)
