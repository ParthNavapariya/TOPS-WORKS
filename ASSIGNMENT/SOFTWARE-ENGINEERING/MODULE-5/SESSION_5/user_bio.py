# Given the string user_bio = 'Music lover | Foodie | Traveller', use a for loop to count and print the number of characters (excluding spaces) in the bio.<br><br><em><strong>Hint:</strong> Use an if statement inside the loop to skip spaces.
user_bio = "music lover | Foodie | Tranveller"
count = 0

for i in user_bio:
    if i == " ":
        print("")
    else:
        print(f"{i}==>{count}")
        count+=1


