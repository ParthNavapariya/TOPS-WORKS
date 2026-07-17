# Simulate a Zomato-style restaurant menu using a nested dictionary: each restaurant name as a key, and its value as another dictionary with keys 'cuisine' and 'rating'. Add two restaurants, then update the rating of one restaurant to a new value.<br><br><em><strong>Hint:</strong> Use dictionary indexing to access and update the nested 'rating' value.</em>

menu = {
    "khodiyar":{
        "cuisine":"gujarati_thali",
        "rating":12
    },
    "umiya":{
        "cuisine":"gujarati_thali",
        "rating":12
    }
}
menu["khodiyar"]["rating"] = 23
print(menu)
