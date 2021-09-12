import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
df_tobefilled = pd.read_csv('prob2_trans.csv')
df_tobefilled1 = df_tobefilled
df_trans = pd.read_csv('prediction_trans_fixed.csv')
df_sup = pd.read_csv('prob3_sup.csv')
df_sup = df_sup.replace(np.nan, 0)
l_id = pd.read_csv('at1_with_mean.csv')['sup_id']
type_id = list(pd.read_csv('at1_with_mean.csv')['type'])
total_loss = 0.
for i in range(len(type_id)):
    if type_id[i] == 'A':
        type_id[i] = 999
    elif type_id[i] == 'B':
        type_id[i] = 99
    else:
        type_id[i] = 9
time = time.time()


for week in range(1, 25):
    # 每周做决策
    num = 0

    # week_str = 'W'
    trans_data = df_trans.iloc[:][str(week - 1)]
    trans_data = [[num, item, 6000] for num, item in enumerate(trans_data)]
    trans_data = sorted(trans_data, key=lambda x: x[1])
    sup_data = df_sup.iloc[:402][str(week)]
    sup_data = [[l_id[i], sup_data[i], type_id[i]] for i in range(402)]
    sup_data = sorted(sup_data, key=lambda x: (x[1], x[2]), reverse=True)
    if week == 24:
        print('24')
        pass

    while 1:
        sup_data = sorted(sup_data, key=lambda x: (x[1], x[2]), reverse=True)

        id = int(sup_data[0][0].split('S')[-1])

        flag = 0

        for i in range(402):
            if sup_data[i][1] != 0:
                flag = 1
                break
        if flag == 0:
        # if [sup_data[i][1] for i in range(402)] == [0] * 402:
            print('Week %d is OK..' % (week))
            break
        idx = None
        trans_selected = None
        distributed_quant = None
        for i in range(len(trans_data)):
            if trans_data[i][2] >= sup_data[0][1]:
                idx = i
                break
        # 先选能容纳的，如果都不能完整容纳就从上往下拆，拆掉max的部分去选能容纳的，如果能容纳相等并存在多个则选损失率最小的
        if idx is not None:
            # found entire space, fill idx
            distributed_quant = sup_data[0][1]

            trans_data[idx][2] -= sup_data[0][1]
            print('第{0}次分配，{1}号全部分配给了物流商{2}，目前{1}号余量为0，物流商{2}号还可容纳{4}'.format(num, sup_data[0][0], trans_data[idx][0], idx, trans_data[idx][2]))
            num += 1
            sup_data[0][1] = 0
            trans_selected = trans_data[idx][0]
            total_loss += distributed_quant * trans_data[idx][1]
        else:
            # for i in range(len(trans_data)):
            # find max remaining
            max_volume_idx = 0
            max_volume = -2e9
            for i in range(8):
                if trans_data[i][2] > max_volume:

                    max_volume_idx = i
                    max_volume = trans_data[i][2]
            # max_volume = trans_data[max_volume_idx][2]
            if week == 24 and trans_data[max_volume_idx][0] == 4:
                print(24)
                pass
            distributed_quant = max_volume
            trans_data[max_volume_idx][2] -= max_volume
            sup_data[0][1] -= max_volume
            print('第{0}次分配，{1}号分配{2}给了物流商{3},目前{1}号余量{4}，物流商{3}号还可容纳{5}'.format(num, sup_data[0][0], max_volume, trans_data[max_volume_idx][0], sup_data[0][1], trans_data[max_volume_idx][2]))
            num += 1
            trans_selected = trans_data[max_volume_idx][0]
            total_loss += distributed_quant * trans_data[max_volume_idx][1]
        col_num = (week-1) * 8 + trans_selected + 1
        print(id, col_num)
        df_tobefilled.iloc[id, col_num] = distributed_quant
            # trans_data[]

    print(trans_data)

    # break

# df_tobefilled.to_csv('prob3_trans_filled_ABC.csv')
print(total_loss * 0.01 / df_sup.iloc[:, 1:].sum().sum())
