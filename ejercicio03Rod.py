"""
Ejercicio 3: Dada la matriz, [[1,2,3],[4,5,6],[7,8,9]], calcule el promedio de la diagonal principal. Hint: Los 3 elementos de la diagonal son 1,5,9
"""

A=[[1,2,3,8,10],[4,5,6,7,-5],[7,8,9,10,3],[7,5,9,8,6],[6,-6,9,8,-10]]

diagonal=[]
sum=0

for i in range(len(A)):
    for j in range(len(A)):
        if i==j:
            n=A[i][j]
            diagonal.append(n)
            sum=sum+n
        j=+1
    i=+1

print(sum)

print("la diagonal de la matriz es")
print(diagonal)

promedio =sum/(len(A))
print(f"el promedio de la diagonal es = {promedio}")
