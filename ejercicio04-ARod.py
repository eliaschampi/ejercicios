"""
Ejercicio 4: Dada la siguiente lista ["Hola", "Amigos", "Hoy", True] , escriba un programa que pida al usuario una palabra, 
dicha palabra debe ser agregada al final y al inicio de la lista.
"""

list=["Hola", "Amigos", "Hoy", True]
palabra=input("ingrese una palabra que desea agregar a la lista ")
list.append(palabra)
list.insert(0,palabra)

print(list)