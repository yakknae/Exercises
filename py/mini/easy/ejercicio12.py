"""Buscar un elemento en una lista
Dada una lista de nombres, verifica si un nombre específico (ingresado por el usuario o definido) está presente y muestra un mensaje adecuado."""

lista = ["Valentino","Thiago","giuliAno"]
nombre_buscar = "Giuliano"
nombre_buscar
if nombre_buscar.lower() in [nombre.lower() for nombre in lista]:
    print("se encontro el nombre en la lista")
else:
    print("no se encontro el nombre")