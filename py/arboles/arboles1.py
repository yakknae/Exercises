class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

# ---- Funciones AVL ----

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

# ---- Altura ----
def altura(nodo):
    if nodo is None:
        return 0
    return getattr(nodo, 'altura', 0)

# ---- Balance ----
def balance(nodo):
    if nodo is None:
        return 0
    return altura(nodo.izq) - altura(nodo.der)

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

# ---- Recorridos ----
def preorden(nodo):
    if nodo:
        print(nodo.valor, end=' ')
        preorden(nodo.izq)
        preorden(nodo.der)

def inorden(nodo):
    if nodo:
        inorden(nodo.izq)
        print(nodo.valor, end=' ')
        inorden(nodo.der)

def postorden(nodo):
    if nodo:
        postorden(nodo.izq)
        postorden(nodo.der)
        print(nodo.valor, end=' ')

# ---- Menú interactivo ----
def mostrar_menu():
    print("\n=== Menú Árbol AVL ===")
    print("1. Insertar valor")
    print("2. Mostrar recorrido Preorden")
    print("3. Mostrar recorrido Inorden")
    print("4. Mostrar recorrido Postorden")
    print("5. Mostrar altura del árbol")
    print("6. Mostrar factor de balance del nodo raíz")
    print("7. Salir")

def main():
    raiz = None
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            valor = input("Ingrese el valor a insertar: ").strip()
            if valor:
                raiz = insertar(raiz, valor)
                print(f"Valor '{valor}' insertado.")
            else:
                print("No se ingresó ningún valor.")

        elif opcion == "2":
            print("Recorrido Preorden:")
            preorden(raiz)
            print()

        elif opcion == "3":
            print("Recorrido Inorden:")
            inorden(raiz)
            print()

        elif opcion == "4":
            print("Recorrido Postorden:")
            postorden(raiz)
            print()

        elif opcion == "5":
            print("Altura del árbol:", altura(raiz))

        elif opcion == "6":
            if raiz:
                print("Balance del nodo raíz:", balance(raiz))
            else:
                print("El árbol está vacío.")

        elif opcion == "7":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")

# ---- Ejecutar programa ----
if __name__ == "__main__":
    main()