from fastapi import APIRouter, Request, Body
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from app.services.spotify_service import (
    get_auth_url,
    get_access_token, get_user_top_tracks
)
import requests

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")



@router.get("/")
def home_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name= "landing.html",
        context ={"request": request}
    )

@router.get("/login")
def login():
    auth_data = get_auth_url()

    return RedirectResponse(
        url=auth_data["auth_url"]
    )

from fastapi.responses import RedirectResponse


@router.get("/callback")
def callback(request: Request, code: str):
    token_data = get_access_token(code)

    access_token = token_data.get("access_token")

    if not access_token:
        return {
            "error": "No access token received",
            "details": token_data
        }

    request.session["token_info"] = token_data

    return RedirectResponse(
        url="/dashboard",
        status_code=302
    )

@router.get("/dashboard")
def dashboard(request: Request):
    token = request.session.get("token_info", {}).get("access_token")

    if not token:
        return RedirectResponse(url="/login")

    top_tracks_data = get_user_top_tracks(token)

    top_tracks = []

    for item in top_tracks_data.get("items", []):
        top_tracks.append({
            "name": item["name"],
            "artist": item["artists"][0]["name"],
            "popularity": item["popularity"],
            "image": item["album"]["images"][0]["url"],
            "spotify_url": item["external_urls"]["spotify"],
            "uri": item["uri"]  # 🔥 KLUCZOWE
        })

    return templates.TemplateResponse(
        request=request,
        name="app.html",
        context={
            "request": request,
            "top_tracks": top_tracks
        }
    )
@router.get("/get_token")
def get_token(request: Request):
    token = request.session.get("token_info", {}).get("access_token")

    if not token:
        return {
            "error": "Token expired, login again"
        }

    return {
        "access_token": token
    }

@router.get("/currently_playing")
def currently_playing(request: Request):
    token = request.session.get("token_info", {}).get("access_token")

    if not token:
        return {
            "error": "Brak tokena. Zaloguj się ponownie"
        }

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        "https://api.spotify.com/v1/me/player",
        headers=headers
    )

    if response.status_code != 200:
        return {
            "error": f"Spotify API error: {response.status_code}"
        }

    data = response.json()

    if not data or not data.get("item"):
        return {
            "error": "Nic nie jest aktualnie odtwarzane"
        }

    track_info = {
        "name": data["item"]["name"],
        "artist": ", ".join(
            artist["name"] for artist in data["item"]["artists"]
        ),
        "album": data["item"]["album"]["name"],
        "image": data["item"]["album"]["images"][0]["url"],
        "is_playing": data.get("is_playing", False),
        "progress_ms": data.get("progress_ms", 0),
        "duration_ms": data["item"].get("duration_ms", 0)
    }

    return track_info

@router.post("/play")
def play(request: Request):
    token = request.session.get("token_info", {}).get("access_token")

    headers = {
        "Authorization": f"Bearer {token}"
    }

    requests.put("https://api.spotify.com/v1/me/player/play", headers=headers)

    return {"status" : "playing"}

@router.post("/pause")
def pause(request: Request):
    token = request.session.get("token_info", {}).get("access_token")

    headers = {
        "Authorization": f"Bearer {token}"
    }

    requests.put("https://api.spotify.com/v1/me/player/pause", headers=headers)

    return {"status": "paused"}


@router.post("/next")
def next_track(request: Request):
    token = request.session.get("token_info", {}).get("access_token")

    headers = {"Authorization": f"Bearer {token}"}

    requests.post("https://api.spotify.com/v1/me/player/next", headers=headers)

    return {"status": "next"}

@router.post("/previous")
def previous_track(request: Request):
    token =  request.session.get("token_info", {}).get("access_token")

    headers = {"Authorization": f"Bearer {token}"}

    requests.post("https://api.spotify.com/v1/me/player/previous", headers=headers)

    return {"status" : "previous"}

@router.get("/recently_played")
def recently_played(request: Request):
    token = request.session.get("token_info", {}).get("access_token")

    if not token:
        return {"error" : "No Token"}

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get("https://api.spotify.com/v1/me/player/recently-played?limit=5", headers=headers)

    data = response.json()

    tracks = []

    for item in data.get("items", []):
        track = item["track"]

        tracks.append({
            "name": track["name"],
            "artist": ", ".join([a["name"] for a in track["artists"]]),
            "image": track["album"]["images"][0]["url"]
        })

    return tracks

@router.post("/seek")
def seek(request: Request, position_ms: int = Body(...)):
    token =  request.session.get("token_info", {}).get("access_token")

    headers = {
        "Authorization" : f"Bearer {token}"
    }

    requests.put(        f"https://api.spotify.com/v1/me/player/seek?position_ms={position_ms}",headers=headers)

    return {"status" : "seeked"}

@router.get("/search")
def search(query: str, request:Request):
    token = request.session.get("token_info", {}).get("access_token")

    if not token:
        return{"error" : "No token"}

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(f"https://api.spotify.com/v1/search?q={query}&type=track&limit=5",headers=headers)

    data = response.json()

    results=[]

    for item in data.get("tracks", {}).get("items", []):
        results.append({
            "name": item["name"],
            "artist": ", ".join([a["name"] for a in item["artists"]]),
            "uri": item["uri"],
            "image": item["album"]["images"][0]["url"]
        })

    return results


@router.post("/play_track")
def play_track(request: Request, uri: str = Body(...)):
    token = request.session.get("token_info", {}).get("access_token")


    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    requests.put("https://api.spotify.com/v1/me/player/play",headers=headers,json={"uris": [uri]})

    return{"status": "playing"}

@router.get("/playlists")
def get_playlists(request:Request):
    token=request.session.get("token_info", {}).get("access_token")

    if not token:
        return{"error" : "No token"}

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get("https://api.spotify.com/v1/me/playlists?limit=10", headers=headers)

    data = response.json()

    playlists=[]

    for item in data.get("items", []):
        playlists.append({
            "name": item["name"],
            "id": item["id"],
            "image": item["images"][0]["url"] if item["images"] else None
        })

    return playlists

@router.post("/play_playlist")
def play_playlist(request: Request, playlist_id: str = Body(...)):
    token = request.session.get("token_info", {}).get("access_token")

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    requests.put(
        "https://api.spotify.com/v1/me/player/play",
        headers=headers,
        json={"context_uri": f"spotify:playlist:{playlist_id}"}
    )

    return {"status": "playing playlist"}

@router.get("/liked_songs")
def liked_songs(request: Request):
    token = request.session.get("token_info", {}).get("access_token")

    if not token:
        return {"error": "No token"}

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        "https://api.spotify.com/v1/me/tracks?limit=10",
        headers=headers
    )

    data = response.json()

    tracks = []

    for item in data.get("items", []):
        track = item["track"]

        tracks.append({
            "name": track["name"],
            "artist": ", ".join([a["name"] for a in track["artists"]]),
            "uri": track["uri"],
            "image": track["album"]["images"][0]["url"]
        })

    return tracks

@router.post("/play_liked")
def play_liked(request: Request):
    token = request.session.get("token_info", {}).get("access_token")

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    requests.put(
        "https://api.spotify.com/v1/me/player/play",
        headers=headers,
        json={"context_uri": "spotify:collection"}
    )

    return {"status": "playing liked songs"}

