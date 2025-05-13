from collections import deque

# Clase base Cliente
class Cliente:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self.dni}"

# Clase ClienteTelefonico (hereda de Cliente)
class ClienteTelefonico(Cliente):
    def __init__(self, nombre, apellido, dni, telefono):
        super().__init__(nombre, apellido, dni)
        self.telefono = telefono

    def __str__(self):
        return f"{super().__str__()}, Teléfono: {self.telefono}"

# Clase ClienteWeb (hereda de Cliente)
class ClienteWeb(Cliente):
    def __init__(self, nombre, apellido, dni, email):
        super().__init__(nombre, apellido, dni)
        self.email = email

    def __str__(self):
        return f"{super().__str__()}, Email: {self.email}"

# Sistema de atención
class SistemaAtencion:
    def __init__(self):
        # Cola unificada para todos los clientes
        self.cola_clientes = deque()
        self.historial = []

    def agregar_cliente_telefonico(self):
        nombre = input("Ingrese el nombre del cliente telefónico: ").lower().strip()
        apellido = input("Ingrese el apellido del cliente telefónico: ").lower().strip()
        dni = input("Ingrese el DNI del cliente telefónico: ").lower().strip()
        telefono = input("Ingrese el número de teléfono: ").lower().strip()
        cliente = ClienteTelefonico(nombre, apellido, dni, telefono)
        self.cola_clientes.append(cliente)
        print(f"Cliente telefónico '{nombre} {apellido}' agregado a la cola.")

    def agregar_cliente_web(self):
        nombre = input("Ingrese el nombre del cliente web: ").lower().strip()
        apellido = input("Ingrese el apellido del cliente web: ").lower().strip()
        dni = input("Ingrese el DNI del cliente web: ").lower().strip()
        email = input("Ingrese el correo electrónico: ").lower().strip()
        cliente = ClienteWeb(nombre, apellido, dni, email)
        self.cola_clientes.append(cliente)
        print(f"Cliente web '{nombre} {apellido}' agregado a la cola.")

    def atender_siguiente_cliente(self):
        if not self.cola_clientes:
            print("No hay clientes en espera.")
            return
        cliente = self.cola_clientes.popleft()
        print(f"Atendiendo a: {cliente}")
        self.historial.append(cliente)

    def ver_historial(self):
        if not self.historial:
            print("El historial de atención está vacío.")
            return

        print("Historial de atención (del más reciente al más antiguo):")
        for cliente in reversed(self.historial):
            print(cliente)

    def mostrar_menu(self):
        while True:
            print("\n--- Menú de Atención ---")
            print("1. Agregar cliente telefónico")
            print("2. Agregar cliente web")
            print("3. Atender al siguiente cliente")
            print("4. Ver historial de atención")
            print("5. Salir")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                self.agregar_cliente_telefonico()
            elif opcion == "2":
                self.agregar_cliente_web()
            elif opcion == "3":
                self.atender_siguiente_cliente()
            elif opcion == "4":
                self.ver_historial()
            elif opcion == "5":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

# Ejecución del sistema
if __name__ == "__main__":
    sistema = SistemaAtencion()
    sistema.mostrar_menu()
