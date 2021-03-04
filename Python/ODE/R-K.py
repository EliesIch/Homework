# Python program to implement Runge Kutta method
# A sample differential equation "dy / dx = (x - y)/2"
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

import time  #code optimize
start = time.perf_counter()


def dydx(x, y):
    return (np.sin(x) - y)


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
h = 0.1

n = 1000
x = np.linspace(1, 50, n)
y1 = np.empty_like(x)
y3 = np.empty_like(x)

for i in range(1, n):
    y1[i] = rungeKutta(x0, y0, x[i], h)

for i in range(1, n):
    y3[i] = rungeKutta(x0, y0, x[i], h)


#odeint
def model(y, x):
    dydx = (np.sin(x) - y)
    return dydx


y2 = odeint(model, y0, x)

# plot results
plt.plot(x, y1, 'g:', label='y1')
plt.plot(x, y2, 'b--', label='y2')
plt.plot(x, y3, 'r-', label='y2')
plt.xlabel('x')
plt.legend([r'R-K', r'Exact',r'R-K5'])

end = time.perf_counter()
print('Running time: %s Seconds' % (end - start))  #time cost
plt.show()

#print ('The value of y at x is:', rungeKutta(x0, y, x, h))

# This code is contributed by Prateek Bhindwar
