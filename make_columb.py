import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.figure(dpi=300)
data_list = [1 * 2.82e4,1.21786 * 2.82e4, 1.40159* 2.82e4]
color = ['#60acfc', '#34d3eb', '#afe39b']
plt.bar(height=data_list, x=[0, 1, 2], color=color, width=0.7)
# plt.plot(data_list)
plt.xticks([])
plt.ylabel('立方米')
plt.show()