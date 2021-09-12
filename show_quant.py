import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# df = pd.read_excel('at1.xlsx', engine='openpyxl', sheet_name='1')
df = pd.read_csv('filtered_at.csv')
# df = pd.read_
A = df[df['type'] == 'A']
B = df[df['type'] == 'B']
C = df[df['type'] == 'C']
len_list = [len(A), len(B), len(C)]
color=[]
plt.figure(dpi=300)
plt.bar(color=['#6fad49', '#4373c7', '#4373c7'], x=[0, 1, 2], height=len_list, width=0.6, tick_label=['A', 'B', 'C'])
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# plt.figure(dpi=150)

plt.xlabel('材料种类')
plt.ylabel('供应商数量')

plt.show()