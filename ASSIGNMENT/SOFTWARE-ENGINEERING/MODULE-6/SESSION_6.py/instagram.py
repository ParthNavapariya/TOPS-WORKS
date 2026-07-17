# Write a loop that takes two lists: usernames and their follower counts, and manually creates a dictionary (without using zip()) that maps each username to its follower count, similar to how Instagram tracks followers.

lst_username = ["parthpatel","nimakant","manishrva"]
lst_follower = ["12k","23k","43m"]
dictonary = {}
for key in range(len(lst_username)):
    dictonary[lst_username[key]] = lst_follower[key]

print(dictonary)


