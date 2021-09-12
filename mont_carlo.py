import random
import time
import numpy as np
import pandas as pd
from tqdm import tqdm
def create_random_combination(sjsnum,ghsnum=402):
    mem_set=set()
    arrays=[]
    n=0
    while n<sjsnum - 3:
        tp = random.randint(0,2**ghsnum-1)
        if tp in mem_set:
            continue
        mem_set.add(tp)
        tpb=str(bin(tp))[2:]
        tpb=(ghsnum-len(tpb))*'0'+tpb
        numlist=[]
        for i in tpb:
            numlist.append(bool(int(i)))
        
        n+=1
        arrays.append(numlist)
    return arrays

t = time.time()
mont_times = 1e5

df = pd.read_csv('predictions_402.csv')
type = pd.read_csv('at1_with_mean.csv')['type']

A_mask = list(type == 'A')
B_mask = list(type == 'B')
C_mask = list(type == 'C')
week = '0'
res = []
max_res = []
l_max_val = []
# for i in range(1, 403):
for week in tqdm(range(0, 24)):
    tmp_max = []
    max_val = -2e9
    ran_arr = create_random_combination(mont_times)

    for mont in tqdm(range(int(mont_times))):
        PA = [ran_arr[mont][i] and A_mask[i] for i in range(402)]
        # print(PA)
        PA = df[str(week)].dot(PA)
        PB = [ran_arr[mont][i] and B_mask[i] for i in range(402)]
        # print(PB)
        PB = df[str(week)].dot(PB)
        PC = [ran_arr[mont][i] and C_mask[i] for i in range(402)]
        PC = df[str(week)].dot(PC)
        if 0.95 * (PA / 0.6 + PB/ 0.66+PC / 0.72) >= 2.82e4:
            # if ()
            res.append([ran_arr[mont], PA - PC])
            if PA - PC > max_val:
                max_val = PA - PC
                tmp_max = ran_arr[mont]
    max_res.append(tmp_max)
    l_max_val.append(max_val)
# print(min(res[0]))
print(l_max_val, max_res)
max_res = np.array(max_res)
np.save('max_result1', max_res)
np.save('max_values1', l_max_val)
print('Used time:',  time.time() - t)
