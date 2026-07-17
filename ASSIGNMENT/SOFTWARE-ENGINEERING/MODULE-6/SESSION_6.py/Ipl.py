# Suppose you have two lists: one with IPL team names and another with their total points this season. Use zip() to combine them into a dictionary, then print only the teams that have more than 10 points.<br><br><em><strong>Hint:</strong> After creating the dictionary, use a for loop to filter and print.</em>

ipl = ["mi","gt","csk"]
point = [1,23,34]

final = dict(zip(ipl,point))
for key,value in final.items():
        if value>10:
                print(key,value)