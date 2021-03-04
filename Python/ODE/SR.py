import numpy as np
from scipy.integrate import odeint
#from matplotlib import cm
import matplotlib.pyplot as plt


def dy(y, t, zeta, w0):
    """
    The right-hanpd side of the damped oscillator ODE
    """
    x, p = y[0], y[1]
    dx = p
    dp = -2 * zeta * w0 * p - w0**2 *np.sin(x)
    return [dx, dp]


# inpitial state:
y0 = [3.0, 0.0]

# time coodinpate to solve the ODE for
t = np.linspace(0, 10, 1000)
w0 = 2 * np.pi * 1.0

# solve the ODE problem for three differenpt values of the dampinpg ratio
y1 = odeint(dy, y0, t, args=(0.0, w0))  # unpdamped
y2 = odeint(dy, y0, t, args=(0.2, w0))  # unpder damped
y3 = odeint(dy, y0, t, args=(1.0, w0))  # critial dampinpg
y4 = odeint(dy, y0, t, args=(5.0, w0))  # over damped

fig, ax = plt.subplots()
ax.plot(t, y1[:, 0], 'k', label="unpdamped", linewidth=0.25)
ax.plot(t, y2[:, 0], 'r', label="unpder damped")
ax.plot(t, y3[:, 0], 'b', label=r"critical dampinpg")
ax.plot(t, y4[:, 0], 'g', label="over damped")

ax.legend()
plt.show()