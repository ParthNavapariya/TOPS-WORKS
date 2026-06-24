# Build a Python script that asks the user to enter a word (like a song name), then uses a for loop to print each character on a new line, but only if the character is a vowel (a, e, i, o, u).<br><br><em><strong>Constraint:</strong> Do not use the 'in' operator inside your if statement — use multiple '==' checks instead.</em>

song = input("Enter song name")
for i in song:
    if i == "a" or i == "i" or i =="u" or i =="o" or i =="e":
        print(i)
