import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import redirect, request, session, url_for
import config

sp_oauth = SpotifyOAuth(
    client_id=config.Config.SPOTIPY_CLIENT_ID,
    client_secret=config.Config.SPOTIPY_CLIENT_SECRET,
    redirect_uri=config.Config.SPOTIPY_REDIRECT_URI,
    scope="user-library-read user-top-read playlist-modify-public",
)

def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

def callback():
    token_info = sp_oauth.get_access_token(request.args['code'])
    session['token_info'] = token_info
    return redirect(url_for("recommend"))

def get_spotify_client():
    token_info = session.get('token_info', {})
    if not token_info:
        return None
    token = token_info.get('access_token')
    if not token:
        return None
    sp = spotipy.Spotify(auth=token)
    return sp

def logout():
    session.clear()
    return redirect(url_for('home'))

def get_top_artists():
    sp = get_spotify_client()
    if sp is None:
        return None

    try:
        # Pobieranie topowych artystów użytkownika (możesz zmienić limit)
        top_artists = sp.current_user_top_artists(limit=5)
        if 'items' not in top_artists:
            return None

        # Zwracamy listę identyfikatorów artystów
        return [artist['name'] for artist in top_artists['items']]
    except spotipy.exceptions.SpotifyException as e:
        print(f"Błąd: {e}")
        return None