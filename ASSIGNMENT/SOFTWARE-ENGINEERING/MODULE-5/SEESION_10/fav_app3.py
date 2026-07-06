# Try to change the first element of your fav_apps tuple to 'YouTube' and observe the error message. Write a comment explaining why this happens based on tuple immutability.

fav_apps = ("instagaram","snapchat","chatgpt","maps","my_file")
fav_apps[0] = "youtube"
print(fav_apps)
#  This will cause an error because tuples are immutable.
# Once a tuple is created, its elements cannot be changed.