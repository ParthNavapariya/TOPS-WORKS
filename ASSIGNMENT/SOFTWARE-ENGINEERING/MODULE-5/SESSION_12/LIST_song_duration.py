# Given a list of song durations in minutes, use a lambda function with the map() function to convert all durations to seconds and print the resulting list.


number = [12,14,15,16,17]
result = list(map(lambda x: x*60,number))
print(result)
