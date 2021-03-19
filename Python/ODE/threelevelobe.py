import numpy as np
from scipy.integrate import  solve_ivp
#from matplotlib import cm
import matplotlib.pyplot as plt

#from mpl_toolkits.mplot3d import Axes3D

import time  #code optimize
start = time.perf_counter()


def model(t, z):  #define ODE
    rho_11 = z[0]
    rho_22 = z[1]
    rho_33 = z[2]
    rho_12 = z[3]
    rho_13 = z[4]
    rho_23 = z[5]
    #if (5.0<t and t<6.0):
    #     omega = 0.5*np.pi
    # else:
    #      omega = 1e-100

    omega_p =  10*np.exp(-0.5 * np.square((t - 14) / 3.0))
    omega_s = 10*np.exp(-0.5 * np.square((t - 9.0) / 3.0))
    drho_11dt = 1j / 2.0 *(omega_p * np.conj(rho_13) -omega_p * rho_13) + gamma_31 * rho_33
    drho_22dt = 1j / 2.0 *(omega_s * np.conj(rho_23) -omega_s * rho_23) + gamma_32 * rho_33
    drho_33dt = -1j / 2.0 *(omega_s * np.conj(rho_23) - omega_s * rho_23 + omega_p *np.conj(rho_13) - omega_p * rho_13) - gamma_33 * rho_33
    drho_12dt = 1j*((delta_p - delta_s) * rho_12 - omega_s / 2.0 * rho_13 +omega_p / 2.0 * np.conj(rho_23))
    drho_13dt = 1j*(delta_p * rho_13 + omega_p / 2.0 * (rho_33 - rho_11) -omega_s / 2.0 * rho_12)
    drho_23dt = 1j*(delta_s * rho_23 + omega_s / 2.0 * (rho_33 - rho_22) -omega_p / 2.0 * np.conj(rho_12))
    dzdt = [drho_11dt, drho_22dt, drho_33dt, drho_12dt, drho_13dt, drho_23dt]
    return dzdt

gamma_31 = 0
gamma_32 = 0
gamma_33 = 0 
delta_p = 0
delta_s = 0
#omega_p = 1
#omega_s = 1
#parameters

#initial conditions
z0 = [1, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]
#time range
n = 10000
t = np.linspace(0, 30, n)
#Pulse shape
#omega = np.empty_like(t)
#omega = 0
#omega = 1*np.exp(-0.5 * np.square((t - 5.0) / 1.0)) #Gaussian
#omega.fill(0)  #Rabi
#omega[200:250] = 0.5* np.pi
#solve ODE

vip = solve_ivp(model, [0, 30], z0, t_eval=t, method='DOP853', first_step=None, max_step=0.01)

blochrho_11 = vip.y[0]
blochrho_22 = vip.y[1]
blochrho_33 = vip.y[2]
blochrho_12 = vip.y[3]
blochrho_13 = vip.y[4]
blochrho_23 = vip.y[5]
omegap =  10*np.exp(-0.5 * np.square((t - 14) / 3.0))
omegas = 10*np.exp(-0.5 * np.square((t - 9.0) / 3.0))

plt.plot(t, blochrho_11, 'r-')
plt.plot(t, blochrho_22, 'b-')
plt.plot(t, blochrho_33, 'g-')
#plt.plot(t, blochrho_13, 'r--')
#plt.plot(t, blochrho_23, 'g--')
plt.plot(t, omegap, 'g--')
plt.plot(t, omegas, 'b--')
plt.plot(t, omegap/omegas, 'r--')
#plt.plot(t, v, 'b:')
#plt.plot(t, u, 'r:')
#plt.plot(t, omega, 'g--')

plt.xlabel('time')
plt.ylim(-0.5,1.1)
#plt.legend([r'$\rho_{11}$', r'$\rho_{22}$', r'$\rho_{33}$', r'$\rho_{12}$', 'u'])
plt.legend([r'$\rho_{11}$', r'$\rho_{22}$', r'$\rho_{33}$', r'$\Omega_{P}$', r'$\Omega_{S}$'])


plt.show()