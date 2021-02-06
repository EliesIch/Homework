import numpy as np

a = np.array(([1,1], [0,1]))

b = np.arange(4).reshape((2, 2))
d= np.random.random((2,4))
c = np.dot(a,b)
print(a)
print(b)
print(d)
print(np.argmin(c))
