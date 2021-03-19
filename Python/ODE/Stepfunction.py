import numpy as np
import matplotlib.pyplot as plt

n = 1000
x = np.linspace(-50, 50, n)
a=50
t0=10


def square(x):

 return (1-((np.exp(10*(x-20)) - np.exp(-10*(x-20))) / (np.exp(10*(x-20)) + np.exp(-10*(x-20)))+1)/2+((np.exp(10*(x-10)) - np.exp(-10*(x-10))) / (np.exp(10*(x-10)) + np.exp(-10*(x-10)))+1)/2-1)







def step(x):

    return ((np.exp(10*(x-30)) - np.exp(-10*(x-30))) / (np.exp(10*(x-30)) + np.exp(-10*(x-30)))+1)/2






def pulse(t):
    return (np.sqrt(np.pi) / 3.0) * np.exp(-np.square((t - 5) / 3.0))+(np.sqrt(np.pi) / 3.0) * np.exp(-np.square((t+ 5) / 3.0))



plt.plot(x,100*pulse(x))
plt.show()
