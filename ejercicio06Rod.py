"""Ejercicio 6
Dado el diccionario que almacena la talla de algunas personas {'Marcelo': 1.80, 'José':1.50, 'Oscar':1.70, 'Jorge': 1.40}, 
escriba un programa que dado un nombre ingresado por el usuario imprime la talla.
Ejemplo:
Ingrese un nombre: Marcelo
Salida: 1.80
"""
talla={'Marcelo':1.80,'Jose':1.50,'Oscar':1.70,'Jorge':1.40}
print(talla)
dato=input("ingrese un nombre :")

print(f"la estatura de {dato} es igual a {talla[dato]}")
print(list(talla)[0])