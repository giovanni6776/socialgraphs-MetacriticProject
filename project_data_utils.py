# Project Data Utils
import pandas as pd

## Return the final Pandas Data Frame to be used in the analysis 
def get_data_game_line():
    metacritic_df = pd.read_csv("data/metacritic_games_full.csv" ,index_col=0)
    return metacritic_df

