"""
Ejercicio 4
Dada una lista de números enteros [15,20,50,80,40,60], escriba un programa que 
dado un dato por el usuario, este sea eliminado de la lista. Tome en cuenta que 
el usuario ingresará datos que se encuentran dentro de la lista

Ejemplo:

Ingrese el dato a eliminar: 60

Salida: [15,20,50,80,40]
"""

list = [15,20,50,80,40,60]

print(list)
number = int(input("Elige el dato que quieres eliminar de la lista: "))

for i in list:
  if i == number:
    list.remove(i)

print(list)



