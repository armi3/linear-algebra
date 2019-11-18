import numpy as np
import matplotlib
matplotlib.use('TkAgg')            #usar esta linea solo en caso de que en computadoras Mac salga un error de: Python is not installed as a framework. The Mac OS X backend
import matplotlib.pyplot as plt


#Resolucion de minimos cuadrados resolviendo la ec. normal (A^T)Ac =y
print('Minimos Cuadrados y Ecuaciones Normales')
A = np.array([[1,1],
              [1,2],
              [1,3]])
b = np.array([[2],
              [2],
              [4]])
print('A \n' + str(A) + '\n')
At=A.transpose()
#Ecuaciones Normales
AtA=np.dot(At, A)
Atb=np.dot(At, b)
print('At*A = \n' +str(AtA))
print('At*b = \n' +str(Atb))

#Solución Ecuacional Normal
print('AT Ax = ATb \n')
x = np.dot(np.linalg.inv(AtA),Atb)
print('Solución de mínimos cuadrados \n')
print(str(x) + '\n')

#Resolucion de minimos cuadrados usando np.linalg.lstsq

print('Recta de Mejor Ajuste')
x = np.array([0, 1, 2, 3, 4, 5, 6])
y = np.array([-1, 1.8, 2.9, 5.4, 8.3, 9.5, 12.9])
A = np.vstack([x, np.ones(len(x))]).T           #Armar la matriz A con los puntos x y una columna de numeros 1
print('A \n' +str(A))
m, b = np.linalg.lstsq(A, y, rcond=None)[0]
print('Los coeficientes de la recta de mejor ajuste son:')
print('pendiente = ', round(m,4), 'intersecto =', round(b,4), '\n')
plt.plot(x, y, 'o',label='Datos Actuales')
plt.plot(x, m*x + b,label='Recta Ajustada')
plt.plot(x,y-m*x-b,'x', label='Errores')
plt.plot(x,0*x,'--')
plt.title('Recta de Mejor Ajuste ')
plt.legend()
plt.savefig("Grafica.png")
plt.show()

