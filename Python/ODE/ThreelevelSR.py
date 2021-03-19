import numpy as np
from scipy.integrate import solve_ivp
#from matplotlib import cm
import matplotlib.pyplot as plt
from scipy import signal
#from mpl_toolkits.mplot3d import Axes3D

import time  #code optimize
start = time.perf_counter()


def omegap(t):
    '''
    if (0.0<t and t<6.0):
        omega = 0.5*np.pi
    else:
        omega =1e-30
        '''
    return (np.sqrt(np.pi) / 3.0) * np.exp(-np.square((t - 10) / 3.0))


def square(x):

 return (1-((np.exp(10*(x-20)) - np.exp(-10*(x-20))) / (np.exp(10*(x-20)) + np.exp(-10*(x-20)))+1)/2+((np.exp(10*(x-10)) - np.exp(-10*(x-10))) / (np.exp(10*(x-10)) + np.exp(-10*(x-10)))+1)/2-1)

def step(x):

    return ((np.exp(10*(x-35)) - np.exp(-10*(x-35))) / (np.exp(10*(x-35)) + np.exp(-10*(x-35)))+1)/2

def model(t, z):  #define ODE
    rho_11 = z[0]
    rho_22 = z[1]
    rho_33 = z[2]
    rho_12 = z[3]
    rho_13 = z[4]
    rho_23 = z[5]
    omega_s = z[6]

    # omega_p=signal.square(2 * np.pi * 5 * t)
    #omega_p = np.pi*square(t)
    omega_p = omegap(t)
    kappa = 0.1*step(t)
    #omega_s = 0
    drho_11dt = 1j / 2.0 * (omega_p * np.conj(rho_13) -
                            omega_p * rho_13) + gamma_31 * rho_33
    drho_22dt = 1j / 2.0 * (omega_s * np.conj(rho_23) -
                            np.conj(omega_s) * rho_23) + gamma_32 * rho_33
    drho_33dt = -1j / 2.0 * (omega_s * np.conj(rho_23) - np.conj(omega_s) * rho_23 +
                             omega_p * np.conj(rho_13) -
                             omega_p * rho_13) - (gamma_31+gamma_32) * rho_33
    drho_12dt = 1j * ((delta_p - delta_s) * rho_12 - np.conj(omega_s) / 2.0 * rho_13 +
                      omega_p / 2.0 * np.conj(rho_23))-Gamma_12*rho_12
    drho_13dt = 1j * (delta_p * rho_13 + omega_p / 2.0 *
                      (rho_33 - rho_11) - omega_s / 2.0 * rho_12)-Gamma_13*rho_13
    drho_23dt = 1j * (delta_s * rho_23 + omega_s / 2.0 *
                      (rho_33 - rho_22) - omega_p / 2.0 * np.conj(rho_12))-Gamma_23*rho_23
    domega_sdt = 1j*100*(rho_23)-1*kappa*omega_s
    dzdt = [drho_11dt, drho_22dt, drho_33dt, drho_12dt, drho_13dt, drho_23dt,domega_sdt]
    return dzdt


gamma_31 = 0.005
gamma_32 = 0.005
delta_p = 0
delta_s = 0

Gamma_13 = 0.0005
Gamma_23 = 0.0005
Gamma_12 = 0.0005
#omega_p = 1
#omega_s = 1
#parameters

#initial conditions
z0 = [0.99, 0.005 + 0j, 0.005 + 0j, 0 + 0j, 0 + 0j, 0.001 + 0.000j,0.00]
#time range
n = 10000
t = np.linspace(0, 60, n)
#Pulse shape
#omega = np.empty_like(t)
#omega = 0
#omega = 1*np.exp(-0.5 * np.square((t - 5.0) / 1.0)) #Gaussian
#omega.fill(0)  #Rabi
#omega[200:250] = 0.5* np.pi
#solve ODE

vip = solve_ivp(model, [0, 60],
                z0,
                t_eval=t,
                method='DOP853',
                first_step=None,
                max_step=0.01)

blochrho_11 = vip.y[0]
blochrho_22 = vip.y[1]
blochrho_33 = vip.y[2]
blochrho_12 = vip.y[3]
blochrho_13 = vip.y[4]
blochrho_23 = vip.y[5]
omega_s = vip.y[6]
fig ,ax=plt.subplots(3)
ax[0].plot(t, blochrho_11, 'r-', label=r'$\rho_{11}$')
#ax.plot(t, blochrho_22, 'b-', label=r'$\rho_{22}$')
#ax.plot(t, blochrho_33, 'g-', label=r'$\rho_{33}$')
ax[0].plot(t, blochrho_33-blochrho_22, 'g-', label=r'$Z$')
ax[0].plot(t, omegap(t), 'g:', label=r'$\Omega_{P}$')
#ax.plot(t, blochrho_13, 'r--', label=r'$\rho_{13}$')
ax[0].plot(t, blochrho_12, 'r--', label=r'$\rho_{12}$')
ax[0].legend()
ax[1].plot(t, (blochrho_23), 'g--', label=r'$Re\rho_{23}$')
ax[1].plot(t, -1j*(blochrho_23), 'b--', label=r'$Im\rho_{23}$')
ax[1].legend()
ax[2].plot(t, ((omega_s)), 'g--', label=r'$Re\Omega_{S}$')
ax[2].plot(t, (-1j*(omega_s)), 'b--', label=r'$Im\Omega_{S}$')
ax[2].plot(t, np.square(abs(omega_s)), 'r-', label=r'$\Omega_{S}^{2}$')
#ax.plot(t, omegas(t), 'b:', label=r'$\Omega_{S}$')

plt.xlabel('time')
#plt.ylim(-0.5, 1.1)
#plt.legend([r'$\rho_{11}$', r'$\rho_{22}$', r'$\rho_{33}$', r'$\rho_{12}$', 'u'])
#plt.legend([r'$\rho_{11}$', r'$\rho_{22}$', r'$\rho_{33}$', r'$\Omega_{P}$', r'$\Omega_{S}$'])
ax[2].legend()

plt.show()