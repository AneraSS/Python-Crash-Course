# funkcija stvara dictionary
def make_album(artist, album_name):
    discography = {'Author':artist, 'Album name':album_name}
    return discography

# unosimo umjetnika i album
while True:
    print ("To quit, enter 'q'. ")
    album_artist = input ("Artist name: ")
    album_title = input ("Album title: ")
    if album_title or (album_artist == 'q'):
        break
    print(make_album(album_artist, album_title))



