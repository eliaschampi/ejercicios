"""
Ejercicio 4: Dada la siguiente lista ["Hola", "Amigos", "Hoy", True] , escriba 
n programa que pida al usuario una palabra, dicha palabra debe ser agregada al 
final y al inicio de la lista.
"""

from subprocess import list2cmdline


list = ["Hola", "Amigos", "Hoy", True]

word = str(input("ingrese una palabra: "))

list.append(word)
list.insert(0, word)

print(list)