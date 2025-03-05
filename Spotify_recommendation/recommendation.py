import spotipy
from spotipy.oauth2 import SpotifyOAuth
from auth import get_spotify_client


def get_top_genres(sp):
    """ Pobiera najczęściej słuchane gatunki użytkownika """
    try:
        top_artists = sp.current_user_top_artists(limit=10, time_range='medium_term')  # Ostatnie 6 miesięcy
        genres = []
        for artist in top_artists["items"]:
            genres.extend(artist["genres"])

        unique_genres = list(set(genres))  # Usuwamy duplikaty

        return unique_genres[:5]  # Maksymalnie 5 gatunków
    except Exception as e:
        print(f"Błąd pobierania gatunków: {e}")
        return []


def get_recommendations():
    """ Pobiera rekomendacje na podstawie ulubionych gatunków """
    sp = get_spotify_client()

    # Pobieramy gatunki użytkownika
    top_genres = get_top_genres(sp)

    if not top_genres:  # Jeśli nie znaleziono gatunków, ustawiamy domyślne
        top_genres = ["pop", "rock", "hip-hop"]

    try:
        recommendations = sp.recommendations(seed_genres=top_genres[:2], limit=10)

        return {
            "top_genres": top_genres,
            "recommended_tracks": [
                {
                    "name": track["name"],
                    "artist": track["artists"][0]["name"],
                    "preview_url": track["preview_url"]  # Link do podglądu piosenki
                }
                for track in recommendations["tracks"]
            ]
        }
    except Exception as e:
        print(f"Błąd pobierania rekomendacji: {e}")
        return {"error": "Nie udało się pobrać rekomendacji."}
