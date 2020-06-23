import numpy as np 
A = [[2,1,2],[3,1,0],[1,1,-1]];
b = np.transpose([-3,5,2])
X = np.linalg.solve(A,b)
print("solution:\n",X)