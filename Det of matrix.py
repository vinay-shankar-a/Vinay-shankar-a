import numpy as np
from numpy.linalg import det
mat=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("matrix:\n",mat)
det=det(mat)
print("determinant of the matrix is:",int(det))