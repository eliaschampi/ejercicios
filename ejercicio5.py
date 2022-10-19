"""
Ejercicio 5
Dada una tupla de números (1,3,5,2,7,5,5,8,4,8,4,8,4), escriba un programa que 
dado un elemento por el usuario, imprima el número de veces que se encuentra en 
la tupla.

Ejemplo:

Ingrese el elemento a contar: 4

Salida: 3
"""

mytuple = (1,3,5,2,7,5,5,8,4,8,4,8,4)

print(mytuple)

value = int(input("Elige un número para saber cuantas veces se repite en la tupla: "))

for i in mytuple:
  if i == value:
    cantidad = mytuple.count(i)

print(f"La cantidad de veces que se repite el número {value} es {cantidad}")
