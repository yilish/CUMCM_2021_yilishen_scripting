import numpy as np
import pandas as pd

df = pd.read_excel('at1.xlsx', engine='openpyxl', sheet_name='1')
mean_mat = np.array([], dtype=np.float)
std_mat = np.array([], dtype=np.float)
type = df['材料分类']
mean_mat.resize(402, 5)
std_mat.resize(402, 5)
mean = []
for i in range(len(df)):
    for j in range(5):
        start = j * 48 + 2
        end = start + 48
        mean_mat[i, j] = df.iloc[i][start:end].sum()
        std_mat[i, j] = df.iloc[i][start:end].std()
    # mean.append(df.iloc[i][2::48].mean())
    # std.append(df.iloc[i][2::48].std())
mean_mat = pd.DataFrame(mean_mat)
threshold = [43.9110303030303, 53.37478571428571, 58.95485714285716]

mean_mat['type'] = type

std_mat = pd.DataFrame(std_mat)
std_mat['type'] = type

mean_mat.to_csv('supplier_mean_matrix.csv', index=None)

std_mat.to_csv('sd_mean_matrix.csv', index=None)
# print(len(mean))
# print(std)
# print(df)