"""
Ejercicio 3: Dada la matriz, [[1,2,3],[4,5,6],[7,8,9]], calcule el promedio de 
la diagonal principal. Hint: Los 3 elementos de la diagonal son 1,5,9
"""

matrix = [[1,2,3, 4],[4,5,6,7],[7,8,9, 10], [10, 11, 12, 13]]
cont = 0
sum = 0
for arr in matrix:
  sum += arr[cont]
  cont += 1

prom = (sum / len(matrix))
print(f"El promedio de la diagonal es {prom}")