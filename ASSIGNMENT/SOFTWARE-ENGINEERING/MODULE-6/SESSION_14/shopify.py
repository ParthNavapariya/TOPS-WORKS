# Write a function add_song_to_playlist(playlists, user, playlist_name, song_title, artist) that adds a song to a user's playlist in a nested dictionary structure like Spotify. If the user or playlist doesn't exist, create them dynamically.

playlists = {}


def add_song_to_playlist(playlists, user, playlist_name, song_title, artist):


    if user not in playlists:
        playlists[user] = {}


    if playlist_name not in playlists[user]:
        playlists[user][playlist_name] = []


    playlists[user][playlist_name].append({
        "song_title": song_title,
        "artist": artist
    })


add_song_to_playlist(
    playlists,
    "parth_1",
    "utsah",
    "beliver",
    "john_deo"
)

print(playlists)