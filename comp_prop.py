import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('filtered_at.csv')

total_productivity = 2.82e4
unit_prod = [0.6, 0.66, 0.72]
props = []
for i in range(len(df)):
    prop = df.iloc[i]['mean'] / (total_productivity * unit_prod[ord(df.iloc[i]['type']) -ord('A')])
    props.append(prop)
df['prop'] = props

df.to_csv('filtered_at.csv', index=None)