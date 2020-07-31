import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y1 = 2 * x

plt.figure(1, figsize=(9, 9))
plt.plot(x, y1, color='red')
plt.xlim((-6, 6))
plt.ylim((-6, 6))
ticks = np.linspace(-6, 6, 5)
plt.xticks(ticks)
plt.yticks([-6, 0, 6], [r'$\alpha$', r'$\beta$', r'$\gamma$'])

plt.xlabel('x')
plt.ylabel('y')

#gca = 'get current axis'

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

x0 = 1
y0 = 2*x0

plt.scatter(x0, y0, s=50, color='b')
plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5)

plt.annotate(r'$2x=%s $' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),textcoords='offset point')

plt.show()
