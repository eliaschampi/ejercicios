"""
Ejercicio 3: Dada la matriz, [[1,2,3],[4,5,6],[7,8,9]],
calcule el promedio de la diagonal principal.
Hint: Los 3 elementos de la diagonal son 1,5,9
"""
mi_matriz = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

for a in mi_matriz:
    indice_matriz_uno = mi_matriz[0]
    indice_matriz_dos = mi_matriz[1]
    indice_matriz_tres = mi_matriz[2]

indice_matriz_uno_uno = indice_matriz_uno[0]
indice_matriz_dos_dos = indice_matriz_dos[1]
indice_matriz_tres_tres = indice_matriz_tres[2]
print("Estos son las diagonales de la matriz: ")
print(indice_matriz_uno_uno, indice_matriz_dos_dos, indice_matriz_tres_tres)


promedio = (indice_matriz_uno_uno+indice_matriz_dos_dos+indice_matriz_tres_tres)/3
print("Este es el promedio de la diagonal de la matriz: ", promedio)