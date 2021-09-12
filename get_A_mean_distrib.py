import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('at1_with_mean.csv')
df = df[df['type'] == 'A']
print(len(df))

plt.figure(dpi=300)
# plt
plt.hist(df['mean'], bins=10)
plt.xlabel('A供货商年平均供货量(立方米)')
plt.ylabel('频率')
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

plt.show()