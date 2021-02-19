# Python program to implement Runge Kutta method
# A sample differential equation "dy / dx = (x - y)/2"
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def dydx(x, y):
    return ((x - y) / 2)


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


# Driver method
x0 = 0
y0 = 0
#x = 3.5
h = 0.2
n=100
x = np.linspace(0, 100, n)
y1 = np.empty_like(x)

for i in range(1, n):
    y1[i] = rungeKutta(x0, y0, x[i], h)


#odeint
def model(y, x):
    dydx = ((x - y) / 2)
    return dydx


y2 = odeint(model, y0, x)

# plot results
plt.plot(x, y1, 'g:', label='y1')
plt.plot(x, y2, 'b-', label='y2')
plt.xlabel('x')
plt.legend([r'R-K', r'Exact'])
plt.show()

#print ('The value of y at x is:', rungeKutta(x0, y, x, h))

# This code is contributed by Prateek Bhindwar
