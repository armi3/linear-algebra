import numpy as np
import sympy as sp

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


#funcion para agregar la matriz aumentada a una matriz cualquiera (mxm)
def Aumentar(a):
    Valor='h'+str(sp.Matrix(a).shape)
    Identidad=sp.eye(int(Valor[2]))
    for x in range(0, int(Valor[2])):
        Identidad=Identidad.col_insert(x, sp.Matrix(a).col(x))
    return Identidad


#Escriba e imprima una matriz 2 x 2
A = np.array([[1, 2], [3, 4]])
print("matriz A: \n" + str(A))

#Calcule la inversa
inva = np.linalg.inv(A)                     #con numpy
print("inversa con numpy: \n " + str(inva))
inva2 = sp.Matrix(A).inv()                  #ccon sympy
print("inversa con sympy: \n " + str(inva2))
inva3 = Aumentar(A).rref()
print("inversa con FERR: \n " + str(inva3))  #con FERR


s = np.random.randint(100, size=(5, 5))   #matriz de 5x5 con valores enteros aleatorios con maximo de 100

#Cree definiciones para construir funciones
def f(x):
    return (s[0][0])*x*x+(s[0][1])*x-(s[0][3])

# Valores que tomara x
x = range(-20, 20)

# Graficar la funcion en el rango especificado
plt.plot(x, [f(i) for i in x])

# Establecemos el color de los ejes.
plt.axhline(0, color="black")

# Especificamos los limites de los ejes.
plt.xlim(-10, 10)
plt.ylim(-100, 100)

#comando para guardar la grafica en la misma carpeta del proyecto.
plt.savefig("output.png")

# Mostramos el grafico realizado.
plt.show()


