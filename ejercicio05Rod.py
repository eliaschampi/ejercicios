""" Ejercicio 5
Dada una tupla de números (1,3,5,2,7,5,5,8,4,8,4,8,4), escriba un programa que dado un elemento por el usuario, 
imprima el número de veces que se encuentra en la tupla.
Ejemplo:
Ingrese el elemento a contar: 4
Salida: 3
"""
tupla=(1,3,5,2,7,5,5,8,4,8,4,8,4)
print(tupla)

n=input("ingrese el elemento a contar = ")
cont=0
for i in range(len(tupla)):
       
    if tupla[i]==int(n):
        
        cont+=1
    

print(f"el numero: {n} se repite {cont} veces")




