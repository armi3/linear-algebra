import random

Num1 = random.randint(1, 10)
Num2 = random.randint(1, 10)

print("\nNum1 = ", Num1)
print("\nNum2 = ", Num2)

Resultados = [Num1 + Num2, Num1 - Num2, Num1 * Num2, Num1 / Num2, Num1 ^ Num2]

j = 0
for i in Resultados:
    print("\nResultados[{}] = {}".format(j, i))
    j += 1

Matriz = [[random.randint(-10, 10) for i in range(7)] for j in range(7)]

print("\nMatriz = ")
for i in Matriz:
    print("\n            ", str(i))

print("\nMatriz2 = ")
j = 0
for i in Matriz:
    i[j] = 666
    j += 1
    print("\n            ", str(i))
