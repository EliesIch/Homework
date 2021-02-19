import numpy as np
from scipy.integrate import odeint
#from matplotlib import cm
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

import time  #code optimize
start = time.perf_counter()


def model(z, t):  #define ODE
    u = z[0]
    v = z[1]
    w = z[2]

    omega = np.pi*t
    dudt = delta * v - gamma_2 * u
    dvdt = omega * w - delta * u - gamma_2 * v
    dwdt = -omega * v - gamma_1 * (w + 1)
    return [dudt, dvdt, dwdt]


#parameters
gamma_1 = 0
gamma_2 = gamma_1 / 2.0 + 0
delta = 0

#initial conditions
z0 = [0, 0, -1]
#time range
t = np.linspace(0, 5* np.pi, 1000)
#solve ODE


z = odeint(model, z0, t)
#bloch vectors
u = z[:, 0]
v = z[:, 1]
w = z[:, 2]
#populations
rho_22 = (1.0 + w) / 2.0
rho_11 = 1 - rho_22

plt.plot(t, rho_11, 'r-')
plt.plot(t, rho_22, 'b--')
plt.plot(t, v, 'b:')
plt.plot(t, u, 'r:')
#plt.xticks(t,color='blue')
plt.xlabel('time')
plt.legend([r'$\rho_g$', r'$\rho_e$', 'u', 'v'])

end = time.perf_counter()
print('Running time: %s Seconds' % (end - start))  #time cost

plt.show()