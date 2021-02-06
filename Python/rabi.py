import numpy as np
from numpy import linalg as LA
from qutip import *
import matplotlib.pyplot as plt
g = 2  #g constant
me = 9.1 * (10**(-31))  #mass of an electron
e = 1.6 * (10**(-19))  #charge of an electron
theta = 0.2 * np.pi  # qubit angle from sigma_z axis (toward sigma_x axis)
gamma1 = 0.0  # qubit relaxation rate
gamma2 = 0.0  # qubit dephasing rate
hc = 1.054571817 * (10**-34)
B = 1
Bz = 0.01
gmr = 28024.951  #gyromagnetic ratio in Mhz/T
options = Options()
options.nsteps = 5000
# initial state
#psi0 = basis(2,1)
psi0 = (np.sqrt(2) / 2) * basis(2, 1) + (np.sqrt(2) / 2) * basis(2, 0)
t = np.linspace(0, 8000, 10000)

# Hamiltonian
sx = sigmax()
sy = sigmay()
sz = sigmaz()
sm = sigmam()

c_op_list = []  # collapse operators
# evolve and calculate expectation values

w0 = (Bz * gmr) / (np.pi) * 10**-6
w1 = (B * gmr) / (np.pi) * 10**-6

H0 = -(1 / 2) * w0 * sz
H1 = -(1 / 2) * w1 * sx
H2 = (1 / 2) * w1 * sy

w = 2 * w0


def H1_Coeff(t, args):
    return np.sin(w * t)


def H2_Coeff(t, args):
    return np.cos(w * t)


H = [H0, [H1, H1_Coeff], [H2, H2_Coeff]]
output = mesolve(H, psi0, t, c_op_list, [sx, sy, sz], options=options)
sx = output.expect[0]
sy = output.expect[1]
sz = output.expect[2]

plt.plot(t, sx, color='b', linestyle=':')
plt.plot(t, sy, color='g', linestyle=':')
plt.plot(t, sz, color='r', linestyle='-')
plt.legend(["sx", "sy", "sz"])
plt.show()
