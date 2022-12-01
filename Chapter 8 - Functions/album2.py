def make_album(artist_name, album_title, song_number=None):
    music_album = {'Author:':artist_name, 'Album title:':album_title}
    if song_number:
        music_album['Song number'] = song_number
    return music_album

discography = make_album('Britney Spears', 'Circus', 12)
print (discography)

discography = make_album('ABBA', 'ABBA')
print (discography)

discography = make_album('Jennifer Lopez', 'J.Lo', 13)
print (discography)