import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('filtered_at.csv')
stds = []
for i in range(len(df)):
    var = df.iloc[i][3:-2].var()
    stds.append(var)
df['vars'] = stds

df.to_csv('filtered_at.csv', index=None)