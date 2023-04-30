import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import secrests
import pandas as pd
from tqdm import tqdm
from retry import retry
import asyncio


client_credentials_manager = SpotifyClientCredentials(
    client_id=secrests.SPOTIFY_CLIENT_ID, client_secret=secrests.SPOTIFY_CLIENT_SECRET
)
sp_client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


"""
Acquire additional data of music infromation from spotify api using the spotify uri
"""


def test():
    print("Testing")


@retry(delay=30, tries=4)
async def get_track_info(uri):
    info = sp_client.audio_features(uri)[0]
    # drop unnessasary features
    info.pop("type", None)
    info.pop("id", None)
    info.pop("track_href", None)
    info.pop("analysis_url", None)
    info.pop("time_signature", None)

    return info


@retry(delay=30, tries=4)
async def get_artist_info(uri):
    info = sp_client.artist(uri)
    # drop unnessasary features
    info.pop("external_urls", None)
    info.pop("href", None)
    info.pop("id", None)
    info.pop("images", None)
    info.pop("name", None)

    return info


@retry(delay=30, tries=4)
async def get_album_info(uri):
    info = sp_client.album(uri)
    # drop unnessasary features
    info.pop("album_group", None)
    info.pop("album_type", None)
    info.pop("artists", None)
    info.pop("available_markets", None)
    info.pop("copyrights", None)
    info.pop("external_ids", None)
    info.pop("external_urls", None)
    info.pop("href", None)
    info.pop("id", None)
    info.pop("images", None)
    info.pop("name", None)
    info.pop("tracks", None)
    info.pop("type", None)

    return info
