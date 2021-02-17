import numpy as np
from scipy.integrate import odeint
#from matplotlib import cm
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D


def model(z, t):
    x = z[0]
    y=z[1]
    dxdt = 3.0* np.exp(-t)
    dydt = 3.0-y
    return [dxdt,dydt]



z0=[0,0]


t = np.linspace(0, 35, 100)

z = odeint(model, z0, t)
x= z[:,0]
y= z[:,1]
plt.plot(t, x,'r-')
plt.plot(t, y,'b--')
plt.xlabel('time')
plt.legend(['x(t)','y(t)'])
plt.show()