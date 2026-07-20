# Refactor the following code to use dynamic nested dictionary creation so that it doesn't throw a KeyError when adding a new user or playlist:<br><br>playlists = {'user1': {'Favourites': ['Song1', 'Song2']}}<br>playlists['user2']['Chill'].append('Song3')<br><br><em><strong>Hint:</strong> Use collections.defaultdict or check if keys exist before accessing.</em>

from collections import defaultdict

playlists = defaultdict(lambda: defaultdict(list))

playlists['user1']['Favourites'].extend(['Song1', 'Song2'])

playlists['user2']['Chill'].append('Song3')

print(playlists)