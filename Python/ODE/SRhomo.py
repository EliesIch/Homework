import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# function that returns dz/dt
def model(z, t):
    x = z[0]
    y = z[1]
    e = z[2]
    dxdt = e*y-gamma_1*x
    dydt = -e*x-gamma_2*(1+y)
    dedt = x-e*k
    dzdt = [dxdt, dydt,dedt]
    return dzdt


# initial condition
z0 = [0.1, 1,0]
k=2
gamma_1=0
gamma_2=0.05
# number of time points
n = 4000

# time points
t = np.linspace(0, 40, n)

# step input

# store solution
x = np.empty_like(t)
y = np.empty_like(t)
e = np.empty_like(t)
# record initial conditions
x[0] = z0[0]
y[0] = z0[1]
e[0] = z0[2]

# solve ODE
for i in range(1, n):
    # span for next time step
    tspan = [t[i - 1], t[i]]
    # solve for next step
    z = odeint(model, z0, tspan)
    # store solution for plotting
    x[i] = z[1][0]
    y[i] = z[1][1]
    e[i] = z[1][2]
    # next initial condition
    z0 = z[1]

# plot results
plt.plot(t, e, 'g:', label='E(t)')
plt.plot(t, x, 'b-', label='R(t)')
plt.plot(t, y, 'r--', label='Z(t)')
plt.ylabel('values')
plt.xlabel('time')
plt.legend(loc='best')
plt.show()