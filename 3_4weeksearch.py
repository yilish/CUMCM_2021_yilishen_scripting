
import pandas as pd
import numpy as np
import time
import os
import matplotlib.pyplot as plt
df_sup = pd.read_csv('at1_with_mean.csv')
types = pd.read_csv('at1_with_mean.csv')['type']
year = 2
week_str = ["W%03d"%i for i in range(48 * year+1, 48 * year +1 +24)]

days_add = []
# week_str = [str(i) for i in range(24)]
unit_prod = [0.6, 0.66, 0.72]

for item in week_str:
    cur_sto = 0
    for i in range(402):
        idx = ord(types[i]) - ord('A')
        prod_ctb = unit_prod[idx]
        cur_sto += df_sup.iloc[i][item] / prod_ctb
    days_add.append(cur_sto)
precision = 4

res = None
for mid in range(10 ** (precision + 1), 0, -1):
    new_mid = mid / (10 ** precision)
    cur_sto = 2.82e4 * 2
    # flag = 0
    flag = 0
    for i in range(24):

        cur_sto += days_add[i]
        cur_sto -= 2.82e4 * new_mid
        # print(cur_sto / 2.82e4 >= 2)
        if cur_sto <= 2.82e4 * 2:
            flag = 1
            break
    if flag != 1:
        print('Mid is found, value is', new_mid)
        res = new_mid
        # res_list.append(res)
        break

if res is None:
    print('Min not found!')
    res = 0
        # res_list.append(-1)
l_remain = []
cur_sto = 2 * 2.82e4
for item in week_str:
    flag = 0
    for i in range(402):
        idx = ord(types[i]) - ord('A')
        prod_ctb = unit_prod[idx]
        cur_sto += df_sup.iloc[i][item] / prod_ctb
    cur_sto -= res * 2.82e4
    l_remain.append(cur_sto / 2.82e4)
    # print(tmp, cur_sto / 2.82e4)
    # tmp += 1
plt.plot(l_remain)
plt.plot([2 for _ in range(24)])
plt.show()