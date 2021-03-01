import numpy as np
from scipy.integrate import odeint
#from matplotlib import cm
import matplotlib.pyplot as plt
from scipy import signal

#from mpl_toolkits.mplot3d import Axes3D

import time  #code optimize
start = time.perf_counter()


def model(z, t):  #define ODE
    u = z[0]
    v = z[1]
    w = z[2]

    #omega = np.exp(-0.5 * np.square((t - 5.0) / 1.0)) #Gaussian
    #omega = 2*np.pi#Rabi
  
    if (t < 5.0):
        omega = 0.0
    elif (t>11.5):
        omega = 0.0
    else:
        omega = np.pi
  
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
t = np.linspace(0, 5 * np.pi, 1000)
#solve ODE
pulse = np.exp(-0.5 * np.square((t - 5.0) / 1.0))
z = odeint(model, z0, t)
#bloch vectors
u = z[:, 0]
v = z[:, 1]
w = z[:, 2]
#populations
rho_22 = (1.0 + w) / 2.0
rho_11 = 1 - rho_22

plt.plot(t, rho_11, 'r-')
plt.plot(t, rho_22, 'b-')
plt.plot(t, v, 'b:')
plt.plot(t, u, 'r:')

plt.plot(t,pulse,'g--')
#plt.xticks(t,color='blue')
plt.xlabel('time')
plt.legend([r'$\rho_g$', r'$\rho_e$', 'v', 'u'])

end = time.perf_counter()
print('Running time: %s Seconds' % (end - start))  #time cost

#square = signal.square( np.pi * 5 * t)
#plt.plot(t,square )


#print(square, sep='\n')




plt.show()