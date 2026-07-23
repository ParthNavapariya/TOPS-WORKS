# Write a function add_song_to_playlist(song_name, playlist) for a Spotify-like app that raises a SongAlreadyExistsError (custom exception) if the song is already present in the playlist.<br><br><em><strong>Hint:</strong> Define SongAlreadyExistsError as a user-defined exception class and use the raise keyword inside your function.</em>
class songAlreadyExistsError(Exception):
    pass

def add_song_to_playlist(song_name,playlst):
                if song_name in playlst:
                        raise songAlreadyExistsError("Eroor")
                playlist.append(song_name)
                return playlist
playlist = ["beliver","sapna","tum ho"]
try :
        user = input("Enter song name ")
        print(add_song_to_playlist(user,playlist))
except songAlreadyExistsError as e:
        print(e)