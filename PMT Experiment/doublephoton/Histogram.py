# Pandas模块绘制直方图和核密度图
# 读入数据
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

Titanic = pd.read_csv('Result03.csv',header=0, usecols=[1])
# 绘制直方图
Titanic.plot(kind='hist',
                 bins=250,
                 color='steelblue',
                 edgecolor='black',
                 density=True,
                 label='直方图')
# 绘制核密度图
#Titanic.plot(kind='kde', color='red', label='Curve')
# 添加x轴和y轴标签
plt.xlabel('Area')
plt.ylabel('Events')
# 添加标题
plt.title('Pulse area distribution')
# 显示图例
plt.legend()
# 显示图形
plt.show()