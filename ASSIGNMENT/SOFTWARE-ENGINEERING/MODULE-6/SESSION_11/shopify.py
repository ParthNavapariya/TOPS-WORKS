# Build a Spotify-style daily playlist shuffle: given a list of 8 song names, use the random module to select and print 3 random songs for today's playlist.<br><br><em><strong>Hint:</strong> Use random.sample() for this task.</em>

import random
shopify = ["falak_tak","Qismat_jo","jaikal_mahakal","ek_din_ekjaan","kun faiya kun","tere_naam","saude_baji","halka_halka"]

print(random.sample(shopify,k=3))

