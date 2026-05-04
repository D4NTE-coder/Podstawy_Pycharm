from fastapi import APIRouter, Request
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
    top_tracks = top_tracks_data.get("items", [])

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