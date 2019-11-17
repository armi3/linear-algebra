import numpy as np
import sympy as sp

A = np.array([[2,0,1],
             [1,1,-4],
             [3,7,-3]])

#determinantes

DETA = np.linalg.det(A)                             #con numpy
print("Determinante con numpy: \n " + str(DETA))
DETA2 = sp.Matrix(A).det()                          #con sympy
print("Determinante con sympy: \n " + str(DETA2))

#Eigenvalores y Eigenvectores

#con numpy
EIG = np.linalg.eigvals(A)
print("Eigenvalores con numpy: \n " + str(EIG))
EIGV = np.linalg.eig(A)
print("Eigenvectores con numpy: \n " + str(EIGV))

#con sympy
EIG2 = sp.Matrix(A).eigenvals()
print("Eigenvalores con sympy: \n " + str(EIG2))
EIGV2 = sp.Matrix(A).eigenvects()
print("Eigenvectores con sympy: \n " + str(EIGV2))

DIAG = sp.Matrix(A).diagonalize()
print("Diagonalizacion con sympy: \n " + str(DIAG))

POL = sp.Matrix(A).charpoly()
print("Polinomio caracteristico: \n " + str(POL))



