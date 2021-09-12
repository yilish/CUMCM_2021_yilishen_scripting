import warnings

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels
import statsmodels.api as sm
import itertools
import statsmodels.tsa.stattools as ts
from tqdm import tqdm
warnings.filterwarnings("ignore")  # 忽略警告信息
df = pd.read_csv('at1_with_mean.csv')
week_str = ["W%03d"%i for i in range(1, 241)]

for p in [0, 1]:
    for q in [0, 1]:
        for d in [0, 1]:

            for season in [6, 12, 18, 24, 48, 96]:
                print(p, d, season)
                predictions = []
                for i in tqdm(range(len(df))):
                    # 计算时序
                    week_data = df.iloc[i][week_str]
                    mean = week_data.mean()
                    adf_summary = ts.adfuller(np.array(week_data).reshape(-1))  # 进行ADF检验并打印结果
                    best_res = None
                    best_aic = None
                    mod = sm.tsa.statespace.SARIMAX(np.asarray(week_data, dtype=float),
                                                    order=(p, q, d),
                                                    seasonal_order=(p, q, d, season),
                                                    enforce_stationarity=False,
                                                    enforce_invertibility=False)
                    best_res = mod.fit()
                    prediction = best_res.forecast(24)
                    if min(prediction) < 0:
                        prediction -= min(prediction)
                    predictions.append(prediction)
                    # con = np.concatenate([week_data, prediction])

                    # print(prediction, sum(prediction))

                predictions = np.array(predictions, dtype=int)
                predictions = pd.DataFrame(predictions)
                predictions.to_csv('preds/predictions_%d_%d_%d_%d.csv' % (p, q, d, season), index=None)