
import spotipy
import spotipy.util as util
import random

SPOTIPY_CLIENT_ID='YOUR_ID_HERE'     #Change this to your Client ID
SPOTIPY_CLIENT_SECRET='YOUR_SECRET_HERE' #Change this to your Client Secret
SPOTIPY_REDIR_URI='http://localhost:8888/callback'

sp = spotipy.Spotify()

user = 'YOUR_USER_ID_HERE'                 #Change to your user id
playlist = 'PLAYLIST_ID_HERE' #Change to your desired playlists id
maxshuffles = 25                    #Change this if you don't want 25 Shuffles
scope = 'user-library-read  playlist-modify-public'

token = util.prompt_for_user_token(user, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIR_URI)

if token:
    sp = spotipy.Spotify(auth=token)

    print('Fetching playlist with id', playlist)
    name = sp.user_playlist(user, playlist)
    print ('Name Found: ' + name['name'])

    results = sp.user_playlist_tracks(user, playlist)
    print('Tracks found')

    tracks=[]
    for item in results['items']:
        print(item['track']['name'])
        tracks.append(item['track']['id'])

    for i in range(1, maxshuffles):
        random.shuffle(tracks)

    print('Song Order Shuffled ', maxshuffles , 'Time(s)')
       
    newplaylist =sp.user_playlist_create(user, name['name'] + ' Shuffled')

    print('New Playlist created', name['name'] + ' Shuffled (' + newplaylist['id'] + ')')

    sp.user_playlist_add_tracks(user, newplaylist['id'], tracks)

    print('All songs added')
    print('Goodbye')
else:
    print ("Can't get token for", user)
