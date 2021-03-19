import numpy as np
from scipy.integrate import odeint, solve_ivp
#from matplotlib import cm
import matplotlib.pyplot as plt

#from mpl_toolkits.mplot3d import Axes3D

import time  #code optimize
start = time.perf_counter()


def model(t, z):  #define ODE
    u = z[0]
    v = z[1]
    w = z[2]

    #if (5.0<t and t<6.0):
    #     omega = 0.5*np.pi
    # else:
    #      omega = 1e-100

    #omega = 2 * np.exp(-0.5 * np.square((t - 8.0) / 1.0))
    dudt = delta * v - gamma_2 * u
    dvdt = omega * w - delta * u - gamma_2 * v
    dwdt = -omega * v - gamma_1 * (w + 1)
    dzdt = [dudt, dvdt, dwdt]
    return dzdt


#parameters
gamma_1 = 0
gamma_2 = gamma_1 / 2.0 + 0
delta = 0
omega = 1e-90
#initial conditions
z0 = [0, 0, -1]
#time range
n = 10000
t = np.linspace(0, 20, n)
#Pulse shape
#omega = np.empty_like(t)
#omega = 0
#omega = 1*np.exp(-0.5 * np.square((t - 5.0) / 1.0)) #Gaussian
#omega.fill(0)  #Rabi
#omega[200:250] = 0.5* np.pi
#solve ODE
'''
u = np.empty_like(t)
v = np.empty_like(t)
w = np.empty_like(t)
# record initial conditions
u[0] = z0[0]
v[0] = z0[1]
w[0] = z0[2]
'''
vip = solve_ivp(model, [0, 20],
                z0,
                t_eval=t,
                method='DOP853',
                first_step=None,
                max_step=0.01)
u = vip.y[0]
v = vip.y[1]
w = vip.y[2]

rho_22 = (1.0 + w) / 2.0
rho_11 = 1 - rho_22

plt.plot(t, rho_11, 'r-')
plt.plot(t, rho_22, 'b-')
plt.plot(t, v, 'b:')
plt.plot(t, u, 'r:')
#plt.plot(t, omega, 'g--')

plt.xlabel('time')
plt.ylim(-1.2, 1.2)
plt.legend([r'$\rho_g$', r'$\rho_e$', 'v', 'u'])
plt.show()