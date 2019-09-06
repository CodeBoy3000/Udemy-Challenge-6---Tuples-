imelda = "More Mayhem", "Imelda May", 2011, (
        (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town"))

album, artist, year, tracks = imelda

print(album)
print(artist)
print(year)

for song in tracks:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))


