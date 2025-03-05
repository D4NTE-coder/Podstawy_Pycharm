import spotipy
from flask import  sessions,jsonify
from werkzeug.exceptions import Unauthorized

from auth import get_spotify_client

def get_recommendations():
    """Pobiera ulubione gatunki użytkownia i generuje rekomendacje."""
    sp = get_spotify_client()
    if not sp:
        return jsonify({"error": "Unauthorized"}), 401

    top_artists = sp.current_user_top_artists(limit=5, time_range="medium_term")

    genres= []
    for artist in top_artists["items"]:
        genres.extend(artist["genres"])

    popular_genres = list(set(genres))[:3]

    recommendations = sp.recommendations(seed_genres=popular_genres, limit=10)
    recommended_tracks = [
        {"name": track["name"],"artist": track["artists"][0]["name"]}
        for track in recommendations["tracks"]

    ]

    return jsonify({"top_genres": popular_genres, "recommended_tracks": recommended_tracks})
