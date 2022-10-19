"""
Ejercicio 7
Dado el diccionario que almacena la talla de algunas personas
{'Marcelo': 1.80, 'José':1.50, 'Oscar':1.70, 'Jorge': 1.40},
escriba un programa que dada una talla por el usuario imprima el nombre.
Ejemplo:
Ingrese una talla: 1.80
Salida: Marcelo
"""

class Personas:

    def __init__(self):
        self.persons = {}
    
    def addPerson(self, name, size):
        key = hash(name)
        self.persons[key] = { "name": name, "size": size }
    
    def findPerson(self, name):
        if hash(name) in self.persons:
            return self.persons[hash(name)]
        return False

    def findBySize(self, size):
        for p in list(self.persons.values()):
            if p["size"] == size:
                return p["name"]
        return "No encontrado"


p = Personas()

p.addPerson("Juan", 45)
p.addPerson("Marcos", 50)
print(p.findBySize(60))