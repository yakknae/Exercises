from collections import deque

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def insertar(raiz, valor):
    if raiz is None:
        return Nodo(valor)
    
    # Inserción normal de ABB
    if valor < raiz.valor:
        raiz.izq = insertar(raiz.izq, valor)
    else:
        raiz.der = insertar(raiz.der, valor)

    # Actualizar altura
    raiz.altura = 1 + max(altura(raiz.izq), altura(raiz.der))

    # Calcular balance
    balance_factor = balance(raiz)

    # Casos de rotación
    # Izquierda-Izquierda
    if balance_factor > 1 and valor < raiz.izq.valor:
        return rotar_derecha(raiz)

    # Derecha-Derecha
    if balance_factor < -1 and valor > raiz.der.valor:
        return rotar_izquierda(raiz)

    # Izquierda-Derecha
    if balance_factor > 1 and valor > raiz.izq.valor:
        raiz.izq = rotar_izquierda(raiz.izq)
        return rotar_derecha(raiz)

    # Derecha-Izquierda
    if balance_factor < -1 and valor < raiz.der.valor:
        raiz.der = rotar_derecha(raiz.der)
        return rotar_izquierda(raiz)

    return raiz

# ---- Rotar izquierda (insertar) ----
def rotar_izquierda(z):
    y = z.der
    T2 = y.izq
    y.izq = z
    z.der = T2
    z.altura = 1 + max(altura(z.izq), altura(z.der))
    y.altura = 1 + max(altura(y.izq), altura(y.der))
    return y

# ---- Rotar derecha (insertar) ----
def rotar_derecha(z):
    y = z.izq
    T3 = y.der
    y.der = z
    z.izq = T3
    z.altura = 1 + max(altura(z.izq), altura(z.der))
    y.altura = 1 + max(altura(y.izq), altura(y.der))
    return y


def balance(nodo):
    if nodo is None:
        return 0
    return altura(nodo.izq) - altura(nodo.der)

def altura(nodo):
    if nodo is None:
        return 0
    return 1 + max(altura(nodo.izq), altura(nodo.der))

def mostrar_hojas(nodo):
    if nodo is None:
        return
    if nodo.izq is None and nodo.der is None:
        print(nodo.valor)
    else:
        mostrar_hojas(nodo.izq)
        mostrar_hojas(nodo.der)

def mostrar_menu():
    print("\n=== Menú Árbol Binario ===")
    print("1. Insertar valor")
    print("2. Mostrar balance del árbol")
    print("3. Mostrar todas las hojas del árbol")
    print("4. Salir")

def main():
    raiz = None
    while True:
        mostrar_menu()
        opcion = input("Ingrese un número del 1 al 4: ")

        if opcion == '1':
            valor = input("Ingrese un valor para insertar: ")
            if valor:
                raiz = insertar(raiz, valor)
                print(f"Valor '{valor}' insertado.")
            else:
                print("Valor no válido.")
        elif opcion == '2':
            print("Balance del árbol:", balance(raiz))
        elif opcion == '3':
            print("Hojas del árbol:")
            mostrar_hojas(raiz)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
