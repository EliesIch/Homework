import numpy as np
from scipy.integrate import odeint
#from matplotlib import cm
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import time
#中间写上代码块
start = time.perf_counter()



def model(y, t):
    if (t < 10.0):
        u = 0.0
    else:
        u = 2.0
    dydt = (-y + u) / 5.0
    return dydt


y0 = 1

t = np.linspace(0, 35, 5000)

y = odeint(model, y0, t)

plt.plot(t, y)
plt.xlabel('time')
plt.ylabel('y(t)')
end = time.perf_counter()
print('Running time: %s Seconds'%(end-start))
plt.show()
