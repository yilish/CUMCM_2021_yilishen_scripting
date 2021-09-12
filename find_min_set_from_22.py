import pandas as pd
import numpy as np
# only computes the first 24 weeks.
df_sup = pd.read_csv('prediction_fixed.csv')
df = pd.read_csv('ranked.csv')
# w = 3
# week_str = ["W%03d"%i for i in range(1 + 24 * w, 25 + 24 * w)]
week_str = [str(i) for i in range(24)]
cur_sto = 2.82e4 * 2
unit_prod = [0.6, 0.66, 0.72]
ac_point = 0

for item in week_str:
    flag = 0
    for i in range(30):
        idx = ord(df_sup.iloc[i]['type']) - ord('A')
        prod_ctb = unit_prod[idx]
        cur_sto += df_sup.iloc[i][item] / prod_ctb
    cur_sto -= 2.82e4
    print(cur_sto / 2.82e4 >= 2)
    if cur_sto >= 2.82e4 * 2:
        ac_points += 1
#
for num in range(24, len(df_sup)):
    cur_sto = 2.82e4 * 2
    flag = 0
    ac_points = 0
    for item in week_str:
        flag = 0
        for i in range(num):
            idx = ord(df.iloc[i]['type']) - ord('A')
            prod_ctb = unit_prod[idx]
            cur_sto += df_sup.iloc[i][item] / prod_ctb
        cur_sto -= 2.82e4

        if cur_sto / 2.82e4 >= 2:
            ac_points += 1
    if ac_points == len(week_str):
        print("Num %d is OK, end"%num)
        break