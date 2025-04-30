#Diseñar un programa en Python que permita gestionar una lista de personas, donde cada persona tiene los siguientes datos: Nombre, Edad, Ciudad

#Clase persona
class Persona:
    def __init__(self,nombre,edad,ciudad):
        self.nombre=nombre.strip()
        self.edad= edad
        self.ciudad = ciudad.strip()

    def __str__(self):
        return F"nombre: {self.nombre}, edad: {self.edad}, ciudad: {self.ciudad}"
    
# FUNCION AGREGAR PERSONA
    @staticmethod
    def agregar_persona(personas):
        print("###########################")
        print("Agregar persona a la lista\n")
        nombre = input("Ingrese el nombre: ").strip()
        edad = int(input("Ingrese la edad: "))
        ciudad = input("Ingrese la ciudad: ").strip()
        nueva_persona = Persona(nombre, edad, ciudad)
        personas.append(nueva_persona)
        print(f"{nombre} ha sido agregado/a a la lista.")
    
# FUNCION BUSCAR CIUDAD   
    @staticmethod
    def buscar_ciudad(personas,):
        print("\n###########################\n")
        ciudad_buscada = input("Ingrese la ciudad de una persona: ").strip()
        print(f"personas que viven en la ciudad buscada ({ciudad_buscada}): ")
        for person in personas:
            if ciudad_buscada.lower() == person.ciudad.lower():
                print(person)

# BUSCAR NOMBRE PERSONA
    @staticmethod
    def buscar_nombre(personas):
        print("\n###########################\n")
        nombre = input("Ingrese el nombre de una persona a buscar: ").strip()
        print(f"personas que tienen el nombre: ({nombre}) ")
        for person in personas:
            if nombre.lower() == person.nombre.lower():
                print(person,"\n")
                
# FUNCION LISTA PERSONAS
    @staticmethod
    def lista_personas(personas):
        print("\n###########################")
        print("\nLista actualizada de personas:")
        for person in personas:
            print(person)

# FUNCION ASIGNAR MASCOTAS
    def asignar_mascota(self,mascota):
        self.mascota = mascota
        print(f"{self.nombre} es dueño/a ahora de {mascota.nombre}.")

# Clase mascota
class Mascota:
    def __init__(self,nombre,edad,tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
    
    def __str__(self):
        return f"nombre: { self.nombre}, edad: {self.edad}, tipo: {self.tipo}"
    
# FUNCION LISTA DE MASCOTAS
    @staticmethod
    def lista_mascotas(mascotas):
        print("\n###########################")
        print("\nLista actualizada de mascotas:")
        for mascota in mascotas:
            print(mascota)
    
# ASIGNAR MASCOTA A PERSONA
def asignar_mascota(personas,mascotas):
    print("\n###########################")
    print("\nAsignar una mascota a una persona")
    nombre_persona = input("Ingrese el nombre de la persona: ").strip()
    nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()
    
    # Buscar persona
    persona_encontrada = None
    for person in personas:
        if nombre_persona.lower() == person.nombre.lower():
            persona_encontrada = person
            break

    if not persona_encontrada:
        print(f"No se encontró a ninguna persona con el nombre '{nombre_persona}'.")
        return
    
    # Buscar mascota
    mascosta_encontrada = None
    for mascota in mascotas:
        if nombre_mascota.lower() == mascota.nombre.lower():
            mascosta_encontrada = mascota
            break
    if not mascosta_encontrada:
        print(f"No se encontró ninguna mascota con el nombre '{nombre_mascota}'.")
        return

    #Asignar la mascota a la persona
    persona_encontrada.asignar_mascota(mascosta_encontrada)


        
# Crear una lista de personas
personas = [
    Persona("Juan",19,"Ituzaingo"),
    Persona("Paz",64,"Moron"),
    Persona("Walter",21,"San Miguel")
]

# Crear una lista de mascotas
mascotas = [
    Mascota("Firulais", 3, "Perro"),
    Mascota("Michi", 5, "Gato"),
    Mascota("Toby", 2, "Perro")
]


# Mostrar la lista actualizada de personas
Persona.lista_personas(personas)

# Mostrar la lista actualizada de mascotas
Mascota.lista_mascotas(mascotas)

# Agregar persona a la lista
Persona.agregar_persona(personas)

# Mostrar las personas que viven en la ciudad buscada
Persona.buscar_ciudad(personas);

# Mostrar las personas que tienen el nombre buscado
Persona.buscar_nombre(personas)

# Asignar mascota a dueño/a
asignar_mascota(personas,mascotas)
