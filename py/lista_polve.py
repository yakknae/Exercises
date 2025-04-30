#Ejercicio 1 - crear una lista, agregar numeros y cuando se ingresa un 0 finaliza.
list = []
a = int(input("Ingresa un número (0 para terminar): ")) 
while(a != 0):
    list.append(a)
    print(f"Has ingresado: {a}")
    a = int(input("Ingresa un número (0 para terminar): ")) 
print("Has terminado de ingresar números.")
print(f"Todos los números: {list}")

#Ejercicio 2 - sumar todos los resultados de la lista
total = sum(list)
print(f"la suma de los números es: {total}")

#Ejercicio 3 - indicar si el numero esta en un indice par
list3 = []
for indice_par in range(2,len(list),2):
    list3.append(list[indice_par])
       
print(f"Los números de indice par: {list3}")   

#Ejercicio 4 - indicar si el numero es par
list2 = []
for pares in list:
    if pares % 2 == 0:
        list2.append(pares)
print(f"Los números pares: {list2}")


#Ejercicio 5 - El usuario pide un numero y me indique en que posicion esta, si no esta en la lista "-1" y si esta te muestra el indice
usuario = int(input("ingrese un numero de la lista: "))
if usuario in list:
    cant = list.count(usuario) 
    print(f"El número {usuario} está en la lista y se repite {cant} veces.")
    for indice, valor in enumerate(list):
        if valor == usuario:
            print(f"Posición: {indice}")
else:
     print("el numero no esta en la lista -1")

#Ejercicio 6 - mismo ejercicio pero usando for y la cantidad de veces que aparece
bad = -1
for indice, valor in enumerate(list):
    if usuario == valor:
        cant +=1
        print(f"El número {usuario} está en la lista en la posición {indice}")
        
# Verificamos si el número se repitió o no
if cant == 0:
    print(f"El número no está en la lista, {bad}")
else:
    print(f"El número {usuario} se repite {cant} veces en la lista.")
