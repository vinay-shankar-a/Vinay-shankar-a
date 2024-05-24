import numpy as np
import sympy as sp
mat = sp.Matrix([[1,2,7],[0,2,5],[0,0,9]])
eigen = mat.eigenvects()
print("Eigen values,no of times repeated,Eigen vector",eigen)
B = np.array([[1,0,0],[2,1,0],[59/56,5/7,1]])
P = B.T
Pinverse = np.linalg.inv(P)
D = Pinverse@mat@P
print("Diagonal matrix:",D)