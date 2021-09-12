
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('prediction_trans_fixed.csv')
for i in range(len(df)):
    df.iloc[i].plot()
plt.show()