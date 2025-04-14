class Jugada:
    def __init__(self,numero,monto,dni):
        self.numero= numero
        self.monto = monto
        self.dni = dni
    
    def __str__(self):
        return f" monto: {self.monto}, dni: {self.dni}, Número: {self.numero}"

class Loteria:
    def __init__(self,numero_ganador):
        self.numero_ganador = numero_ganador

    def contar_coincidencias(self,jugada_numero):
        num_str = str(jugada_numero)
        ganador_str = str(self.numero_ganador)

        coincidencias = 0
        for i in range(1, min(len(num_str), len(ganador_str)) + 1):
            if num_str[-i] == ganador_str[-i]:
                coincidencias += 1
            else:
                break
        return coincidencias
    
    def calcular_pozo(self,monto,coincidencias):
        if coincidencias == 1:
            return monto * 7
        elif coincidencias == 2:
            return monto * 70
        elif coincidencias == 3:
            return monto * 700
        else:
            return 0
    
    def imprimir_resultado(self,jugada,coincidencias,pozo):
        print(f"El ganador es la persona con DNI: {jugada.dni}, con el número: {jugada.numero}")
        print(f"Coincidieron {coincidencias} dígitos. El pozo es: {pozo}")

    def verificar_ganador(self,jugadas):
        for jugada in jugadas:
            coincidencias = self.contar_coincidencias(jugada.numero)
            if coincidencias > 0:
                pozo = self.calcular_pozo(jugada.monto, coincidencias)
                self.imprimir_resultado(jugada,coincidencias,pozo)

# Cargar lista de jugadas
jugadas = [
    Jugada(350, 500, "46213395"),
    Jugada(1012, 300, "11222333"),
    Jugada(51, 1500, "77765653")
]

# Crear instancia de Lotería
loteria = Loteria(350)

# Función principal
loteria.verificar_ganador(jugadas)
