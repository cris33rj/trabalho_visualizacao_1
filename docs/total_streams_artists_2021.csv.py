# %%
import numpy as np 
import pandas as pd 
import sys

# %%
spotify_data = pd.read_csv('docs/data/spotify-2023.csv', encoding='ISO-8859-1')

# %%
spotify_data['streams'] = pd.to_numeric(spotify_data['streams'], errors='coerce')
spotify_data = spotify_data[spotify_data['released_year'] == 2021]
artist_streams = spotify_data.groupby('artist(s)_name')['streams'].sum().sort_values(ascending=False).head(10)


# %%
columns = ['artist(s)_name', 'Total Streams (in billions)']

df_artist_streams  = pd.DataFrame(list(artist_streams.items()), columns=columns)

# %%
df_artist_streams.to_csv(sys.stdout,header=True,index=False)

