import pandas as pd
import numpy as np
df_sup = pd.read_csv('predictions_402.csv')
df_sup = df_sup.iloc[:, 1:]
df = pd.read_csv('arrange.csv')
df = df.iloc[:, 1:]
# for i in range(len(df)):
#     for j in range(len(df.iloc[i])):
#         df.iloc[i, j] = True if df.iloc[i, j] == 1 else False
df_sup = df_sup.mask(np.array(df, dtype=bool))
df_sup = df_sup.replace(0, np.nan)
df_sup.to_csv('prob3_sup.csv')
# print(df['0'])
