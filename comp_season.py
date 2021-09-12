import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('filtered_at.csv')
stds = []
season_diffs = []
offset = 3
for i in range(len(df)):
    season_diff = 0.
    for j in range(240):
        season_diff += (df.iloc[i][(j + 48) % 240 + offset] - df.iloc[i][j + offset]) ** 2
    season_diffs.append(season_diff)
df['season_diffs'] = season_diffs
# print(season_diffs)
df.to_csv('filtered_at.csv', index=None)