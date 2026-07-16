# Take a tuple of your last 7 WhatsApp call durations in minutes (e.g., (12, 5, 0, 20, 7, 3, 15)), convert it to a list, remove all calls shorter than 5 minutes, then convert it back to a tuple and print the result.<br><br><em><strong>Hint:</strong> Use a for loop or list comprehension to filter the list before converting back to tuple.</em>

whatshapp = (12, 5, 0, 20, 7, 3, 15)
whatshapp_lst = list(whatshapp)

final = [i for i in whatshapp_lst if i >= 5]
print(tuple(final))
