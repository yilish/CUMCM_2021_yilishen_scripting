def dataDirection_1(datas, offset=0):
	def normalization(data):
		return 1 / (data + offset)

	return list(map(normalization, datas))


def dataDirection_2(datas, x_min, x_max):
	def normalization(data):
		if data <= x_min or data >= x_max:
			return 0
		elif data > x_min and data < (x_min + x_max) / 2:
			return 2 * (data - x_min) / (x_max - x_min)
		elif data < x_max and data >= (x_min + x_max) / 2:
			return 2 * (x_max - data) / (x_max - x_min)

	return list(map(normalization, datas))


def dataDirection_3(datas, x_min, x_max, x_minimum, x_maximum):
	def normalization(data):
		if data >= x_min and data <= x_max:
			return 1
		elif data <= x_minimum or data >= x_maximum:
			return 0
		elif data > x_max and data < x_maximum:
			return 1 - (data - x_max) / (x_maximum - x_max)
		elif data < x_min and data > x_minimum:
			return 1 - (x_min - data) / (x_min - x_minimum)

	return list(map(normalization, datas))


import pandas as pd
import numpy as np


def topsis(data, weight=None):
	# 归一化
	data = data / np.sqrt((data ** 2).sum())

	# 最优最劣方案
	Z = pd.DataFrame([data.min(), data.max()], index=['负理想解', '正理想解'])

	# 距离
	weight = [0.491702, 0.002396, 0.003406, 0.007486, 0.491545, 0.003466]

	Result = data.copy()
	Result['正理想解'] = np.sqrt(((data - Z.loc['正理想解']) ** 2 * weight).sum(axis=1))
	Result['负理想解'] = np.sqrt(((data - Z.loc['负理想解']) ** 2 * weight).sum(axis=1))

	# 综合得分指数
	Result['综合得分指数'] = Result['负理想解'] / (Result['负理想解'] + Result['正理想解'])
	Result['排序'] = Result.rank(ascending=False)['综合得分指数']

	return Result, Z, weight