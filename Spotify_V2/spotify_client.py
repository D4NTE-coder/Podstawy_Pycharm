def create_playlist(sp, name="Moja Nowa Playlista", description="Automatycznie wygenerowana"):
    """Tworzy nową playlistę na koncie użytkownika."""
    user_id = sp.current_user()["id"]
    playlist = sp.user_playlist_create(user_id, name, public=True, description=description)
    return playlist["id"]

def add_tracks_to_playlist(sp, playlist_id, track_uris):
    """Dodaje utwory do podanej playlisty."""
    sp.playlist_add_items(playlist_id, track_uris)

def get_current_playing_track(sp):
    """Pobiera aktualnie odtwarzany utwór."""
    track = sp.current_playback()
    if track and track["is_playing"]:
        item = track["item"]
        return {
            "name": item["name"],
            "artist": item["artists"][0]["name"],
            "album": item["album"]["name"],
            "image": item["album"]["images"][0]["url"]
        }
    return None

def get_recently_played_tracks(sp, limit=10):
    """Pobiera ostatnio odtwarzane utwory użytkownika."""
    results = sp.current_user_recently_played(limit=limit)
    tracks = []
    for item in results['items']:
        track = item['track']
        tracks.append({
            "name": track['name'],
            "artist": track['artists'][0]['name'],
            "album": track['album']['name'],
            "image": track['album']['images'][0]['url']
        })
    return tracks