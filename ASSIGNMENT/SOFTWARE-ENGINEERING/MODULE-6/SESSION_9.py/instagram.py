# Use a lambda function with the filter() function to get only the usernames with more than 1000 followers from this list: [('raj', 800), ('simran', 1500), ('veer', 1200), ('ananya', 950)]. Print the usernames that would get the 'K' badge like Instagram.

username = [("raj",800),("simaran",1500),("veer",1200),("ananya",950)]
result = filter(lambda user: user[1] > 1000, username)
for user in result:
    print(user[0])