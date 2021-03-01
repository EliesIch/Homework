import numpy as np
from scipy.integrate import odeint
#from matplotlib import cm
import matplotlib.pyplot as plt

#from mpl_toolkits.mplot3d import Axes3D

import time  #code optimize
start = time.perf_counter()


def model(z, t, omega):  #define ODE
    u = z[0]
    v = z[1]
    w = z[2]

    dudt = delta * v - gamma_2 * u
    dvdt = omega * w - delta * u - gamma_2 * v
    dwdt = -omega * v - gamma_1 * (w + 1)
    dzdt = [dudt, dvdt, dwdt]
    return dzdt


#parameters
gamma_1 = 0.2
gamma_2 = gamma_1 / 2.0 + 0
delta = 1
#initial conditions
z0 = [0, 0, -1]
#time range
n = 1000
t = np.linspace(0, 20, n)
#Pulse shape
omega = np.empty_like(t)
#omega = 1*np.exp(-0.5 * np.square((t - 5.0) / 1.0)) #Gaussian
omega.fill(np.pi)  #Rabi
#omega[200:250] = 0.5* np.pi
#solve ODE
u = np.empty_like(t)
v = np.empty_like(t)
w = np.empty_like(t)
# record initial conditions
u[0] = z0[0]
v[0] = z0[1]
w[0] = z0[2]

for i in range(1, n):
    # span for next time step
    tspan = [t[i - 1], t[i]]
    # solve for next step
    z = odeint(model, z0, tspan, args=(omega[i], ))
    # store solution for plotting
    u[i] = z[1][0]
    v[i] = z[1][1]
    w[i] = z[1][2]
    # next initial condition
    z0 = z[1]

rho_22 = (1.0 + w) / 2.0
rho_11 = 1 - rho_22

plt.plot(t, rho_11, 'r-')
plt.plot(t, rho_22, 'b-')
plt.plot(t, v, 'b:')
plt.plot(t, u, 'r:')
plt.plot(t, omega, 'g--')

plt.xlabel('time')
plt.ylim(-1.2, 1.2)
plt.legend([r'$\rho_g$', r'$\rho_e$', 'v', 'u'])

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("auto")

# draw sphere
a, b = np.mgrid[0:2 * np.pi:100j, 0:np.pi:100j]
d = np.cos(a) * np.sin(b)
e = np.sin(a) * np.sin(b)
f = np.cos(b)
ax.plot_wireframe(d, e, f, color="r", linestyle=':', linewidth=0.5)


# ANIMATION FUNCTION
def func(num, dataSet, line):
    # NOTE: there is no .set_data() for 3 dim data...
    line.set_data(dataSet[0:2, :num])
    line.set_3d_properties(dataSet[2, :num])
    return line


# THE DATA POINTS

dataSet = np.array([u, v, w])

# GET SOME MATPLOTLIB OBJECTS
#ax = Axes3D(fig)

# NOTE: Can't pass empty arrays into 3d version of plot()
line = plt.plot(dataSet[0], dataSet[1], dataSet[2], lw=2,
                c='b')[0]  # For line plot

# AXES PROPERTIES]
# ax.set_xlim3d([limit0, limit1])

# Creating the Animation object
line_ani = animation.FuncAnimation(fig,
                                   func,
                                   frames=n,
                                   fargs=(dataSet, line),
                                   interval=1e-50,
                                   blit=False)
#line_ani.save(r'AnimationNew.mp4')




from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d


class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

'''
arrow = Arrow3D([0, -np.pi], [0, 0], [0, delta],
            mutation_scale=20,
            lw=1,
            arrowstyle="-|>",
            color="k")
ax.add_artist(arrow)

'''



ax.set_xlabel(r'u(-$\Omega$)')
ax.set_ylabel(r'v(0)')
ax.set_zlabel(r'w($\Delta$)')











end = time.perf_counter()
print('Running time: %s Seconds' % (end - start))  #time cost

plt.show()