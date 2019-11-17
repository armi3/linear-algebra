import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol

def f1(x):
    return 1-x                      #f(x)=1-x
def f2(x):
    return x-4                      #f(x)=x-4
def f3(x):
    return x+4                      #f(x)=x+4
def f4(x):
    return 6-x                      #f(x)=6-4

plt.figure(1)                       #Abre una ventana para la 1ra grafica
x = range(-10, 10)                  #x toma los valores de -10 a 10
plt.title('Graficas de las cuatro rectas')
plt.plot(x, [f1(i) for i in x])     #grafica de todas las funciones con los valores de x
plt.plot(x, [f2(i) for i in x])
plt.plot(x, [f3(i) for i in x])
plt.plot(x, [f4(i) for i in x])

plt.xlim(-3, 7)                     #limites de visualizacion de la grafica en el eje x
plt.ylim(-3, 7)                     #limites de visualizacion de la grafica en el eje y
x = Symbol('x')                     #encontrar puntos de insterseccion entre funciones
x1, =  solve(f1(x)-f2(x))           #coordenada x de interseccion entre f1 y f2
x2, =  solve(f1(x)-f3(x))           #coordenada x de interseccion entre f1 y f3
x3, =  solve(f2(x)-f4(x))
x4, =  solve(f3(x)-f4(x))

y1 = f1(x1)                         #coordenada y de interseccion entre f1 y f2
y2 = f1(x2)                         #coordenada y de interseccion entre f1 y f3
y3 = f2(x3)
y4 = f3(x4)

print(str(x1)+","+str(y1))          #imprime corrdenada x,y de interseccion entre f1 y f2
print(str(x2)+","+str(y2))          #imprime corrdenada x,y de interseccion entre f1 y f3
print(str(x3)+","+str(y3))
print(str(x4)+","+str(y4))

plt.figure(2)                       #Abre otra ventana para la 2da grafica
plt.plot(x1,y1,'go',markersize=10)  #grafica la corrdenada x,y de interseccion entre f1 y f2
plt.plot(x2,y2,'go',markersize=10)  #grafica la corrdenada x,y de interseccion entre f1 y f3
plt.plot(x3,y3,'go',markersize=10)
plt.plot(x4,y4,'go',markersize=10)

plt.title('Grafica de la region entre las cuatro rectas')
plt.fill([x2,x4,x3,x1],[y2,y4,y3,y1],'red',alpha=0.5) #rellena el espacio entre los 4 puntos

plt.grid()                          #Agrega una cuadricula a la grafica
plt.savefig("grafica.png")          #guarda la imagen en la carpeta del proyecto
plt.show()                          #muestra en pantalla la imagen de la grafica