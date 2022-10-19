""" Dada una lista de números enteros [15,20,50,80,40,60], escriba un programa que dado un dato por el usuario,
este sea eliminado de la lista. Tome en cuenta que el usuario ingresará datos que se encuentran dentro de la lista
Ejemplo:
Ingrese el dato a eliminar: 60
Salida: [15,20,50,80,40]"""

from operator import truediv


datos=[15,20,50,80,40,60]

aux=True
while aux ==True:
    print(datos)
    dato=int(input("ingrese el numero que desea eliminar = "))
    if dato in datos:
        aux=False
    else:
        print("debe ingresar un dato de la lista\n")

datos.pop(datos.index(dato))
print("--------------------")
print(datos)
