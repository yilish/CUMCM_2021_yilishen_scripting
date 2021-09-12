import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# only computes the first 24 weeks.
df = pd.read_csv('ranked.csv')
df_sup = pd.read_csv('prediction_fixed.csv')

w = 3
# week_str = ["W%03d"%i for i in range(1 + 24 * w, 25 + 24 * w)]
week_str = [str(i) for i in range(24)]
cur_sto = 2.82e4 * 2
unit_prod = [0.6, 0.66, 0.72]
res = 0
tmp = 1
l_remain = []
l_remain_origin = []
plt.figure(dpi=300)

for item in week_str:
    flag = 0
    for i in range(30):
        idx = ord(df.iloc[i]['type']) - ord('A')
        prod_ctb = unit_prod[idx]
        cur_sto += df_sup.iloc[i][item] / prod_ctb
    cur_sto -= 2.82e4
    l_remain.append(cur_sto / 2.82e4)
    # print(tmp, cur_sto / 2.82e4)
    tmp += 1
cur_sto = 2.82e4 * 2
plt_list = []
# '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
styles = ['dotted', '--', '-.', ':','dashed', 'solid']
for i in range(5):
    w = i
    l_remain_origin = []
    week_str = ["W%03d"%i for i in range(1 + 24 * w, 25 + 24 * w)]
    cur_sto = 2.82e4 * 2
    for item in week_str:
        flag = 0
        for j in range(30):
            idx = ord(df.iloc[j]['type']) - ord('A')œ
            prod_ctb = unit_prod[idx]
            cur_sto += df.iloc[j][item] / prod_ctb
        cur_sto -= 2.82e4
        l_remain_origin.append(cur_sto / 2.82e4)
        # print(tmp, cur_sto / 2.82e4)
        tmp += 1
    # y = np.linspace(0, 24, 1)



    plot_ins, = plt.plot(l_remain_origin, linestyle=styles[i])
    plt_list.append(plot_ins)
    # plt.legend()
x = [2 for _ in range(24)]
plt.plot(x, color='grey')
plot_ins, = plt.plot(l_remain, linestyle=styles[5], marker='*')
plt_list.append(plot_ins)
# plt_list.append(plt.plot(l_remain))
legend_list = ['第%d年结果' % (i+1) for i in range(5)]
legend_list.append('我们的结果')
plt.legend(handles=plt_list, labels=legend_list, loc='best')
plt.xlabel('周')
plt.ylabel('剩余可用库存(周)')
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

plt.show()
