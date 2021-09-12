import warnings

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels

df = pd.read_excel('transport.xlsx', engine='openpyxl')
week_str = ["W%03d"%i for i in range(1, 241)]
predictions = []
for i in range(len(df)):
    # 计算时序
    week_data = df.iloc[i][week_str]
    # print(week_data)
    # week_data.plot()
    mean = week_data.mean()
    # week_data -= mean
    # print(week_data)
    # plt.show()
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
    print(len(prediction))
    con = np.concatenate([week_data, prediction])
    plt.plot(con)
    # plt.plot(prediction)
    print(prediction, sum(prediction))
    plt.show()

predictions = np.array(predictions)
predictions = pd.DataFrame(predictions)
predictions.to_csv('predictions_trans.csv', index=None)
