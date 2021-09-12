import warnings

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('predictions_trans.csv').to_numpy()


for i in range(len(df)):
    min_val = min(df[i])
    if min_val < 0:
        df[i] -= min_val
df = pd.DataFrame(df)
print(df)
df.to_csv('prediction_trans_fixed.csv', index=None)
