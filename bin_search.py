import os

import pandas as pd
import numpy as np
import time
import os
import matplotlib.pyplot as plt
week_str = [str(i) for i in range(24)]
unit_prod = [0.6, 0.66, 0.72]
low = 2
high = 99
res = None
l_dir = os.listdir('preds')
res_list = []
types = pd.read_csv('at1_with_mean.csv')['type']

A_mask = list(types == 'A')
B_mask = list(types == 'B')
C_mask = list(types == 'C')
# for file in l_dir:
for i in range(1):
    df_sup = pd.read_csv('predictions_402.csv')
    # df_sup = pd.read_csv('preds/' + file)
    days_add = []
    for item in week_str:
        cur_sto = 0
        if df_sup.iloc[:][item].sum() > 48000:
            rem_trans = 48000

            if df_sup.iloc[:][item][A_mask].sum() <= rem_trans:
                cur_sto += df_sup.iloc[:][item][A_mask].sum() / 0.6
                rem_trans -= df_sup.iloc[:][item][A_mask].sum()
            else:
                cur_sto += rem_trans / 0.6
            if df_sup.iloc[:][item][B_mask].sum() <= rem_trans:
                cur_sto += df_sup.iloc[:][item][B_mask].sum() / 0.66
                rem_trans -= df_sup.iloc[:][item][B_mask].sum()
            else:
                cur_sto += rem_trans / 0.66
            if df_sup.iloc[:][item][C_mask].sum() <= rem_trans:
                cur_sto += df_sup.iloc[:][item][C_mask].sum() / 0.72
                rem_trans -= df_sup.iloc[:][item][C_mask].sum()
            else:
                cur_sto += rem_trans / 0.72
        else:
            for i in range(402):
                idx = ord(types[i]) - ord('A')
                prod_ctb = unit_prod[idx]
                cur_sto += df_sup.iloc[i][item] / prod_ctb
        days_add.append(cur_sto)
    precision = 5
    t = time.time()
    if 1:
        for mid in range(10 ** (precision + 1), 10 ** precision, -1):
            new_mid = mid / (10 ** precision)
            cur_sto = 2.82e4 * 2
            # flag = 0
            flag = 0
            for i in range(24):

                cur_sto += days_add[i]
                cur_sto -= 2.82e4 * new_mid
                # print(cur_sto / 2.82e4 >= 2)
                if cur_sto <= 2.82e4 * 2:
                    if new_mid == 1.39955:
                        print(1)
                        pass
                    flag = 1
                    break
            if flag != 1:
                print('Mid is found, value is', new_mid)
                res = new_mid
                res_list.append(res)
                break

    if res is None:
        print('Min not found!')
        res = 0
        res_list.append(-1)
    l_remain = []
    cur_sto = 2 * 2.82e4
    for i in range(24):
        cur_sto += days_add[i]
        cur_sto -= res * 2.82e4
        l_remain.append(cur_sto / 2.82e4)
        # print(tmp, cur_sto / 2.82e4)
        # tmp += 1
    plt.plot(l_remain)
    plt.plot([2 for _ in range(24)])
    if res == 10.0 or res == 0:
        pass
    else:

        # plt.savefig('figs/' + file.split('.')[0] + str(res) + '.jpg')
        plt.show()

    print('time:', time.time() - t)
    plt.clf()
print(res_list)