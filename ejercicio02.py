"""
Ejercicio 2: Haga un programa en Python que le pida al usuario tantos enteros como quiera, luego cree dos listas,
una con la lista de números propuestos
y la otra con el número de ocurrencias.
Por ejemplo, si el usuario ingresa 4,4,8,4,9,7,7, la primera lista
debe ser [4,8,9,7] y el segundo [3,1,1,2]
"""

list = []
list1 = []
contador = 0
list2 = []
A = int(input("Ingrese la cantidad de números"))

for i in range(A):
  B = int(input("Ingrese los números"))
  list.append(B)


for i in list:
  if i not in list1:
    list1.append(i)
    a = list.count(i)
    list2.append(a)
print(list)
print(list1)
print(list2)
  


