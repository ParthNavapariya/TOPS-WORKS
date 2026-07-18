# Refactor your character count script to use a function named char_count_dict(text) that returns the frequency dictionary, and then print the dictionary sorted by character (A-Z or a-z).

def char_count_dict(text):
    dicts = {}

    for i in text:
        if i in dicts:
            dicts[i] += 1
        else:
            dicts[i] = 1

    return dicts


result = char_count_dict("parth")

for char in sorted(result):
    print(char, result[char])