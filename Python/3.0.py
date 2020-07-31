import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
y2 = x**2

plt.figure(3, figsize=(16, 9))

plt.xlim((-1, 1))
plt.ylim((-1, 1))
ticks = np.linspace(-1, 1, 5)
plt.xticks(ticks)

plt.yticks([-1, 0, 1], [r'$\alpha$', r'$\beta$', r'$\gamma$'])

plt.xlabel('x')
plt.ylabel('y')

l1, = plt.plot(x,y1,color='red')
l2, = plt.plot(x, y2, color='blue', linewidth=1.0, linestyle='--')

plt.legend(handles=[l1,l2,] ,  labels=['a','b'],loc='best' )
plt.show()
