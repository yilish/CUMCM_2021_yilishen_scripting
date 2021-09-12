import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_sup = pd.read_csv('filtered_at.csv')
df_ord = pd.read_csv('filtered_ord.csv')
pos_difs = []
neg_difs = []
exceed_ability = []
# lesses = []
for i in range(len(df_sup)):
    W_list = ['W%03d' % i for i in range(1, 241)]
    pos_dif = 0
    neg_dif = 0
    greater = 0
    # less = 0
    for item in W_list:
        pos_dif += df_sup.iloc[i][item] - df_ord.iloc[i][item] if df_sup.iloc[i][item] - df_ord.iloc[i][item] > 0 else 0
        neg_dif += df_sup.iloc[i][item] - df_ord.iloc[i][item] if df_sup.iloc[i][item] - df_ord.iloc[i][item] < 0 else 0
        if df_sup.iloc[i][item] > 6000:
            greater += 1
    pos_difs.append(pos_dif)
    neg_difs.append(neg_dif)
    exceed_ability.append(greater)

df_sup['pos_difs'] = pos_difs
df_sup['neg_difs'] = neg_difs
df_sup['exceed_ability'] = exceed_ability
df_sup.to_csv('filtered_at.csv', index=None)
