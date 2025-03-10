from blinker.base import ANY_ID

from auth import get_spotify_client
from auth import get_top_artists
import spotipy
def get_recommendations():
    sp = get_spotify_client()
    if sp is None:
        return None

    top_artists = get_top_artists()
    if not top_artists:
        return None

    # Jeśli top_artists ma mniej niż 5, możesz spróbować wziąć tyle, ile masz
    top_artists = top_artists[:5]  # Zmniejsz liczbę do 5, jeśli jest więcej
    print("Top artists:", top_artists)  # Dobrze jest wiedzieć, co dokładnie jest przekazywane

    try:
        recommendations = sp.recommendations(
            seed_artists=top_artists,  # Przekazuj ID artystów
            seed_genres=[],  # Możesz podać konkretne gatunki, np. ['pop', 'rock']
            seed_tracks=[],  # Możesz dodać przykładowe utwory, np. ['3n3pApJzAy39yM2zotE9Kn']
            limit=10,
            country='PL'  # Podaj kod kraju, np. 'PL' dla Polski
        )
    except spotipy.exceptions.SpotifyException as e:
        print(f"Błąd: {e}")
        return None

    # Przetwarzanie rekomendacji
    return [{
        'track_name': track['name'],
        'artist': track['artists'][0]['name'],
        'album': track['album']['name'],
        'preview_url': track['preview_url']
    } for track in recommendations['tracks']]