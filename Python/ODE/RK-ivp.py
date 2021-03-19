# Python program to implement Runge Kutta method
# A sample differential equation "dy / dx = (x - y)/2"
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint, solve_ivp

import time  #code optimize
start = time.perf_counter()
np.seterr(divide='ignore', invalid='ignore')


def dydx(x, y):
    return (np.sin(x))


# Finds value of y for a given x using step size h
# and initial value y0 at x0.
def rungeKutta(x0, y0, x, h):
    # Count number of iterations using step size or
    # step height h
    n = (int)((x - x0) / h)
    # Iterate for number of iterations
    y = y0
    for i in range(1, n + 1):
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * dydx(x0 + h, y + k3)

        # Update next value of y
        y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

        # Update next value of x
        x0 = x0 + h
    return y


def rungeKutta6(x0, y0, x, h):
    # Count number of iterations using step size or
    # step height h
    n = (int)((x - x0) / h)
    # Iterate for number of iterations
    y = y0
    for i in range(1, n + 1):
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + 0.25 * h, y + 0.25 * k1)
        k3 = h * dydx(x0 + 0.25 * h, y + 0.125 * k1 + 0.125 * k2)
        k4 = h * dydx(x0 + 0.5 * h, y - 0.5 * k2 + k3)
        k5 = h * dydx(x0 + 0.75 * h, y + (3.0 / 16.0) * k1 + (9.0 / 16.0) * k4)
        k6 = h * dydx(
            x0 + h, y - (3.0 / 7.0) * k1 + (2.0 / 7.0) * k2 +
            (12.0 / 7.0) * k3 - (12.0 / 7.0) * k4 + (8.0 / 7.0) * k5)

        # Update next value of y
        y = y + (1.0 / 90.0) * (7 * k1 + 32 * k3 + 12 * k4 + 32 * k5 + 7 * k6)

        # Update next value of x
        x0 = x0 + h
    return y


# Driver method
x0 = 0
y0 = 0
#x = 3.5
h = 0.01

n = 1000
x = np.linspace(0, 50, n)
y1 = np.empty_like(x)
y2 = -np.cos(x) + 1
y3 = np.empty_like(x)

c0 = ([0.0])
vip = solve_ivp(dydx, [0, 50], c0, t_eval=x, method='DOP853',first_step=None, max_step=0.001)
y4 = vip.y[0]

for i in range(1, n):
    y1[i] = rungeKutta(x0, y0, x[i], h)
'''
for i in range(1, n):
    y3[i] = rungeKutta6(x0, y0, x[i], h)
'''


def model(y, x):

    return (np.sin(x))


y5 = odeint(model, y0, x, hmax=0.001, mxords=6)

plt.subplot(211)
# plot results
#plt.plot(x, y1, 'g:')
plt.plot(x, y2, 'b:')
#plt.plot(x, y5 + 0.5, 'r--')
plt.plot(x, y4 + 1, 'r--')
plt.xlabel('x')
plt.legend([r'RK', r'Exact', r'Odeint', r'Vip_RK'])
plt.subplot(212)
plt.plot(x, (y4 - y2) , 'b--')
plt.plot(x, (y1 - y2) , 'r-')
#plt.plot(x, (y5 - y2) / y2, 'g:')
plt.legend([r'vip', r'RK', r'odeint'])

#plt.ylim(-0.1, 0.1)
end = time.perf_counter()
print('Running time: %s Seconds' % (end - start))  #time cost
plt.show()

#print ('The value of y at x is:', rungeKutta(x0, y, x, h))

# This code is contributed by Prateek Bhindwar
