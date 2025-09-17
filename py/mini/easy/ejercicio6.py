"""Mostrar claves y valores de un diccionario
Crea un diccionario con información personal (nombre, edad, ciudad) y muestra cada clave y su valor en líneas separadas."""

personas = {
    'nombre' : 'valentino',
    'edad': 18,
    'profesion': 'ingeniero'
}

for clave, valor in personas.items():
    print(f"{clave} es {valor}")