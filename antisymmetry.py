import numpy as np
A=[[0,-5],[5,0]]
print((np.array(A).T == -np.array(A)).all())