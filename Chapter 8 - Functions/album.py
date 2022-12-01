def make_album(artist_name, album_title):
    music_album = {'Author:':artist_name, 'Album title:':album_title}
    return music_album

discography = make_album('Britney Spears', 'Circus')
print (discography)

discography = make_album('ABBA', 'ABBA')
print (discography)

discography = make_album('Jennifer Lopez', 'J.Lo')
print (discography)