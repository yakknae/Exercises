#Diseñar un programa en Python que permita gestionar una lista de personas, donde cada persona tiene los siguientes datos: Nombre, Edad, Ciudad

#clase principal persona
class Persona:
    def __init__(self,nombre,edad,ciudad):
        self.nombre=nombre
        self.edad= edad
        self.ciudad = ciudad

    def __str__(self):
        return F"nombre: {self.nombre}, edad: {self.edad}, ciudad: {self.ciudad}"
    
# Crear una lista de personas
personas = [
    Persona("Juan",19,"Ituzaingo"),
    Persona("Paz",64,"Moron"),
    Persona("Walter",21,"San Miguel")
]

# Mostrar las personas que viven en la ciudad buscada
ciudad_buscada= "Ituzaingo"
print(f"personas que viven en la ciudad buscada {ciudad_buscada}: ")
for person in personas:
    if ciudad_buscada == person.ciudad:
        print(person)