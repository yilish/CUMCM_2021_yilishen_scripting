import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('supplier_mean_matrix.csv')

A = []
B = []
C = []

for i in range(len(df)):
    if df.iloc[i]['type'] == 'A':
        # for j in range(5):
        A.append(df.iloc[i][0:5].mean())

    if df.iloc[i]['type'] == 'B':
        B.append(df.iloc[i][0:5].mean())

    if df.iloc[i]['type'] == 'C':
        C.append(df.iloc[i][0:5].mean())
# 总量
A = np.array(A)
B = np.array(B)
C = np.array(C)
A = A[A >= np.mean(A) * 0.01]
B = B[B >= np.mean(B) * 0.01]
C = C[C >= np.mean(C) * 0.01]
print('threshold:', np.mean(A) * 0.01, np.mean(B) * 0.01,  np.mean(C) * 0.01)

total = np.concatenate([A, B, C])
# print(len(A[A >= np.mean(A) * 0.2]))
# print(A, B, C)
print(total)


plt.hist(total, range=[0, 10000])
# plt.bar(height=[len(A)/3, len(B)/3, len(C)/3], x=[i for i in range(3)], tick_label=['A', 'B', 'C'])
plt.show()
