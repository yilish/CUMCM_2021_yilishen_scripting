import numpy as np
import pandas as pd

df = pd.read_excel('at1.xlsx', engine='openpyxl', sheet_name='1')

mean = []
for i in range(len(df)):
    mean.append(df.iloc[i][2:].mean())
    # for j in range(5):
    #     start = j * 48 + 2
    #     end = start + 48
    #     mean_mat[i, j] = df.iloc[i][start:end].sum()
    #     std_mat[i, j] = df.iloc[i][start:end].std()
    # mean.append(df.iloc[i][2::48].mean())
    # std.append(df.iloc[i][2::48].std())

mean = np.array(mean)
# print(mean)
df['mean'] = mean
# print(df['type'])
A = df[df['type'] == 'A']
B = df[df['type'] == 'B']
C = df[df['type'] == 'C']
threshold = 0.01
A = A[A['mean'] > 41.46852168949771 * threshold]
B = B[B['mean'] > 53.37478571428571 * threshold]
C = C[C['mean'] > 58.95485714285716 * threshold]
A = A.append(B).append(C)
print(A)
A.to_csv('filtered_at.csv')
# print(A['mean'].mean())
# print(A)
# column = df.columns
# column[0] = 'sup
# _id'
# column[1] = 'type'

# print(df.columns)
# df.to_csv('at1_with_mean.csv')
# mean_mat = pd.DataFrame(mean_mat)
# threshold = [43.9110303030303, 53.37478571428571, 58.95485714285716]

# mean_mat['type'] = type

# std_mat = pd.DataFrame(std_mat)
# # std_mat['type'] = type
#
# mean_mat.to_csv('supplier_mean_matrix.csv', index=None)
#
# std_mat.to_csv('sd_mean_matrix.csv', index=None)
# # print(len(mean))
# # print(std)
# # print(df)