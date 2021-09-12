import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# only computes the first 24 weeks.
df = pd.read_csv('at1_with_mean.csv')
df_sup = pd.read_csv('predictions_402.csv')

types = pd.read_csv('at1_with_mean.csv')['type']

A_mask = list(types == 'A')
B_mask = list(types == 'B')
C_mask = list(types == 'C')
w = 3
# week_str = ["W%03d"%i for i in range(1 + 24 * w, 25 + 24 * w)]
week_str = [str(i) for i in range(24)]
cur_sto = 2.82e4 * 2
unit_prod = [0.6, 0.66, 0.72]
res = 0
tmp = 1
l_remain = []
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
            cur_sto += df_sup.iloc[:][item][B_mask].sum() / 0.6
            rem_trans -= df_sup.iloc[:][item][B_mask].sum()
        else:
            cur_sto += rem_trans / 0.66
        if df_sup.iloc[:][item][C_mask].sum() <= rem_trans:
            cur_sto += df_sup.iloc[:][item][C_mask].sum() / 0.6
            rem_trans -= df_sup.iloc[:][item][C_mask].sum()
        else:
            cur_sto += rem_trans / 0.72
    else:
        for i in range(402):
            idx = ord(types[i]) - ord('A')
            prod_ctb = unit_prod[idx]
            cur_sto += df_sup.iloc[i][item] / prod_ctb
    days_add.append(cur_sto)

plt.figure(dpi=300)
plt_list = []

styles = ['-', '--']
for i in range(24):
    flag = 0
    cur_sto += days_add[i]
    cur_sto -= 2.82e4
    l_remain.append(cur_sto / 2.82e4)
    plot_ins, = plt.plot(l_remain, linestyle='-')
    plt_list.append(plot_ins)
    # print(tmp, cur_sto / 2.82e4)
    tmp += 1

l_remain = []
cur_sto = 2 * 2.82e4
for i in range(24):
    flag = 0
    cur_sto += days_add[i]
    cur_sto -= 1.21786 * 2.82e4
    l_remain.append(cur_sto / 2.82e4)
    plot_ins, = plt.plot(l_remain, linestyle='-.')
    plt_list.append(plot_ins)

    # print(tmp, cur_sto / 2.82e4)
    tmp += 1
# y = np.linspace(0, 24, 1)
x = [2 for _ in range(24)]
plt.plot(x, color='black')
plt.legend(handles=plt_list, labels=['周产能为1.21786倍', '周产能为1倍'], loc='lower left')

plt.show()