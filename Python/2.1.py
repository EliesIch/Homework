import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
#创建画布
fig = plt.figure(figsize=(8, 8))
#使用axisartist.Subplot方法创建一个绘图区对象ax
ax = axisartist.Subplot(fig, 111)  
#将绘图区对象添加到画布中
fig.add_axes(ax)
#gca = 'get current axis'

ax.axis[:].set_visible(False)

#ax.new_floating_axis代表添加新的坐标轴
ax.axis["k"] = ax.new_floating_axis(0,0)
#给x坐标轴加上箭头
ax.axis["k"].set_axisline_style("-|>", size = 2.0)
#添加y坐标轴，且加上箭头
ax.axis["E"] = ax.new_floating_axis(1,0)
ax.axis["E"].set_axisline_style("-|>", size = 2.0)
#设置x、y轴上刻度显示方向
ax.axis["k"].set_axis_direction("top")
ax.axis["E"].set_axis_direction("right")
#生成x步长为0.1的列表数据
x = np.arange(-15,15,0.1)
#生成sigmiod形式的y数据
y=x**2
#设置x、y坐标轴的范围
plt.xlim(-5,5)
plt.ylim(-5, 5)
plt.xticks([])
plt.yticks([])
#绘制图形
plt.plot(x,y, c='b')

plt.show()
