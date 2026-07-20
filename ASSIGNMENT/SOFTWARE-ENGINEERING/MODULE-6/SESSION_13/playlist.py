# Given a list of playlists where each playlist is a list of song durations in seconds (e.g., [[210, 180, 240], [150, 200], [300, 120, 90]]), use a nested list comprehension to create a new list containing only the durations greater than 200 seconds from all playlists.

playlist = [
    [210, 180, 240], [150, 200], [300, 120, 90]
    ]


lst = [j for i in playlist  for j in i if j > 200]
print(lst)

