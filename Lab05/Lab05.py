import numpy as np
import sympy as sp


# funcion para agregar la matriz aumentada a una matriz cualquiera (mxm)
def Aumentar(a):
    Valor = 'h' + str(sp.Matrix(a).shape)
    Identidad = sp.eye(int(Valor[2]))
    for x in range(0, int(Valor[2])):
        Identidad = Identidad.col_insert(x, sp.Matrix(a).col(x))
    return Identidad


# Escriba e imprima una matriz 2 x 2
A = np.array([[1, 2], [3, 4]])
print("matriz A: \n" + str(A))

# Calcule la inversa
print("EJEMPLO 1: Inversa de la matriz A usando tres métodos \n")
inva = np.linalg.inv(A)  # con numpy
print("inversa con numpy: \n " + str(inva))
inva2 = sp.Matrix(A).inv()  # ccon sympy
print("inversa con sympy: \n " + str(inva2))
inva3 = Aumentar(A).rref()
print("inversa con FERR: \n " + str(inva3))  # con FERR
print("Inversa de la matriz A usando tres métodos")
print('------------------------------------------------------ \n')  # imprime  una línea  horizontal

# Calcula el rango de la matriz
Rango = np.linalg.matrix_rank(A)
# Número de columnas de la matriz
Numcols = A.shape[1]
# Núlidad de la matriz A
Nulidad = Rango - Numcols

print("EJEMPLO 2: Rango y Nulidad de la Matriz A \n")
print("# Columnas:  " + str(Numcols))
print("Rango:       " + str(Rango))  # calcula el rango de una matriz
print("Nulidad:     " + str(Nulidad))

# calcula una base para el espacio nulo de A
print("Base Espacio nulo: \n" + str(sp.Matrix(A).nullspace()))

print('------------------------------------------------------ \n')
