import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('ranked.csv')
week_str = ["W%03d"%i for i in range(1, 241)]
my_x_ticks = np.arange(1, 241, 30)
plt.figure(dpi=300)

for i in range(len(df)):
    plt.plot(df.iloc[i][week_str])
    plt.xticks([])
plt.xticks(my_x_ticks)
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']


plt.show()