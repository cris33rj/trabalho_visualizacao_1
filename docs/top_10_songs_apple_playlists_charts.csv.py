# %%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations
import sys

import warnings

warnings.filterwarnings("ignore")  


spotify_data = pd.read_csv('docs/data/spotify-2023.csv', encoding='ISO-8859-1')


def remover_virgula(string):
    if isinstance(string, str):
        string = float(string.replace(",", ""))        
    return string 

# %%
spotify_data['in_deezer_playlists'] = spotify_data['in_deezer_playlists'].apply(remover_virgula)


# %%
spotify_data['in_shazam_charts'] = spotify_data['in_shazam_charts'].apply(remover_virgula)



# %%
# Descobrindo as 10 músicas mais tocadas do Spotify com base em presença em playlists e paradas.
top_songs_spotify = spotify_data[['track_name', 'artist(s)_name', 'in_spotify_playlists', 'in_spotify_charts']]
top_songs_spotify['spotify_total'] = top_songs_spotify['in_spotify_playlists'] + top_songs_spotify['in_spotify_charts']
top_songs_spotify = top_songs_spotify.sort_values(by='spotify_total', ascending=False).head(10)

# Descobrindo as 10 músicas mais tocadas da Apple com base em presença em playlists e paradas.
top_songs_apple = spotify_data[['track_name', 'artist(s)_name', 'in_apple_playlists', 'in_apple_charts']]
top_songs_apple['apple_total'] = top_songs_apple['in_apple_playlists'] + top_songs_apple['in_apple_charts']
top_songs_apple = top_songs_apple.sort_values(by='apple_total', ascending=False).head(10)

# Descobrindo as 10 músicas mais tocadas do Deezer com base em presença em playlists e paradas.
top_songs_deezer = spotify_data[['track_name', 'artist(s)_name', 'in_deezer_playlists', 'in_deezer_charts']]
top_songs_deezer['deezer_total'] = top_songs_deezer['in_deezer_playlists'] + top_songs_deezer['in_deezer_charts']
top_songs_deezer = top_songs_deezer.sort_values(by='deezer_total', ascending=False).head(10)

# Descobrindo as 10 músicas mais tocadas do Shazam com base em presença em playlists e paradas.
top_songs_shazam = spotify_data[['track_name', 'artist(s)_name', 'in_shazam_charts']]
top_songs_shazam['shazam_total'] = top_songs_shazam['in_shazam_charts']
top_songs_shazam = top_songs_shazam.sort_values(by='shazam_total', ascending=False).head(10)












top_songs_apple.to_csv(sys.stdout,header=True,index=False)

