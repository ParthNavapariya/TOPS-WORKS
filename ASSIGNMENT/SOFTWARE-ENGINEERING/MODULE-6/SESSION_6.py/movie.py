# Given three lists — movie titles, genres, and ratings — use zip() to create a list of dictionaries where each dictionary contains keys 'title', 'genre', and 'rating' for a movie, then print the list.<br><br><em><strong>Constraint:</strong> Do not use any external libraries.</em>

movie_title = ["don3","yevdu","bahubali"] 
genrs = ["action","comedy","horror"]
rating = [2,3,4]


result = []
for title,gen,rat in zip(movie_title,genrs,rating):
    result.append({
        "title":title,
        "geners":gen,
        "rating":rat
    })
print(result)