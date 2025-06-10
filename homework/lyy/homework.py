import numpy as np
a = np.arange(0,9).reshape(3,3)
print(a)
b = np.arange(0,3).reshape(3,1)
print(b)
c = np.einsum('ij,jk->ik',a,b)
print(c)