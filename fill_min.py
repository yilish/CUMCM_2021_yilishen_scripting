import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# only computes the first 24 weeks.
df_sup = pd.read_csv('ranked.csv')
df_tobefilled = pd.read_csv('prob2.csv')
df_pred = pd.read_csv('prediction_fixed.csv', dtype=int)
w = 0
week_str = ["W%03d"%i for i in range(1 + 24 * w, 25 + 24 * w)]
for i in range(30):
    id = df_sup.iloc[i]['sup_id']
    for j in range(len(week_str)):
        curweek = week_str[j]
        if int(df_pred.iloc[i][j]) == 0:
            df_tobefilled.loc[df_tobefilled['sup_id'] == id, curweek] = pd.NA
            continue

        df_tobefilled.loc[df_tobefilled['sup_id'] == id, curweek] = int(df_pred.iloc[i][j])
df_tobefilled.dtype = int
df_tobefilled.to_csv('prob2.csv', index=None)