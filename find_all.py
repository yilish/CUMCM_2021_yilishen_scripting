import pandas as pd
import numpy as np
# only computes the first 24 weeks.
df_sup = pd.read_csv('ranked.csv')
# df_req = pd.read_csv('ranked_req.csv')
w = 3
week_str = ["W%03d"%i for i in range(1 + 24 * w, 25 + 24 * w)]
# print(df_sup['sup_id'] == df_req['sup_id'])
total_productivity = 2.82e4 * 24
cur_prod = 2.82e4 * 2
unit_prod = [0.6, 0.66, 0.72]

for i in range(len(df_sup)):
    idx = ord(df_sup.iloc[i]['type']) - ord('A')
    prod_ctb = unit_prod[idx]
    sum_in24 = 0
    for item in week_str:
        sum_in24 += df_sup.iloc[i][item]
    cur_prod += sum_in24 / prod_ctb
    if cur_prod > total_productivity:
        print(i)
        break

print(cur_prod)