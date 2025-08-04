from dotenv import load_dotenv
load_dotenv()
import os

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")


def get_playlist_for_mood(mood):
    
    playlists = {
        "happy": {
            "name": "Feelin’ Good",
            "url": "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0"
        },
        "sad": {
            "name": "Sad Indie",
            "url": "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1"
        },
        "neutral": {
            "name": "Lo-fi Beats",
            "url": "https://open.spotify.com/playlist/37i9dQZF1DXdxcBWuJkbcy"
        }
    }

    return playlists.get(mood, playlists["neutral"])
