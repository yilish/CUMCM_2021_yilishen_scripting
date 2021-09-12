import warnings

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels

df = pd.read_csv('ranked.csv')
week_str = ["W%03d"%i for i in range(1, 241)]
predictions = []
for i in range(len(df)):
    week_data = df.iloc[i][week_str]
    mean = week_data.mean()
    import statsmodels.tsa.stattools as ts

    adf_summary = ts.adfuller(np.array(week_data).reshape(-1))  # 进行ADF检验并打印结果
    from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
    import itertools

    p = q = range(0, 2)  # p、q一般取值不超过2
    d = range(1, 2)
    pdq = list(itertools.product(p, d, q))
    seasonal_pdq = [(x[0], x[1], x[2], 48) for x in list(itertools.product(p, d, q))]
    print(seasonal_pdq)
    import statsmodels.api as sm
    warnings.filterwarnings("ignore")  # 忽略警告信息
    best_res = None
    best_aic = None
    mod = sm.tsa.statespace.SARIMAX(np.asarray(week_data, dtype=float),
                                    order=(1, 1, 1),
                                    seasonal_order=(1, 1, 0, 48),
                                    enforce_stationarity=False,
                                    enforce_invertibility=False)
    best_res = mod.fit()
    prediction = best_res.forecast(24)
    predictions.append(prediction)
    con = np.concatenate([week_data, prediction])
    plt.plot(con)
    print(prediction, sum(prediction))
    plt.show()
    plot_acf(week_data, lags=48).show()  # 其中lags参数是指横坐标最大取值
    plot_pacf(week_data, lags=48).show()
    break
predictions = np.array(predictions)
predictions = pd.DataFrame(predictions)
predictions.to_csv('predictions1.csv')
