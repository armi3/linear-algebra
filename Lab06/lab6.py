import numpy as np
import sympy as sp
import time as tm


def ReglaCrammer(A,b):
    sol = []
    deta = round(np.linalg.det(A), 1)

    for i in range(len(b)):
        B = A.copy()
        B[:, i] = b
        detb = round(np.linalg.det(B), 1)
        sol.append(detb / deta)
    return sol


A = np.array([[2, -1, 5],
              [3, -2, 1],
             [-2,  2, 3]])


b = np.array([[2],
             [-3],
              [5]])

#determinantes
DETA = np.linalg.det(A)                             #con numpy
print("Determinante con numpy: \n " + str(DETA))
DETA2 = sp.Matrix(A).det()                          #con sympy
print(" \n Determinante con sympy: \n " + str(DETA2))

#calcular la inversa
inva = np.linalg.inv(A)                     #con numpy
print("inversa con numpy: \n " + str(inva))
inva2 = sp.Matrix(A).inv()                  #ccon sympy
print("inversa con sympy: \n " + str(inva2))


#solucion del sistema
inicio=tm.time()
print(ReglaCrammer(A, b.transpose()))
print("cramer: "+str(tm.time()-inicio))

inicio=tm.time()
print(np.dot(inva, b))
print("numpy: "+str(tm.time()-inicio))

inicio=tm.time()
print(np.dot(inva2, b))
print("sympy: "+str(tm.time()-inicio))




