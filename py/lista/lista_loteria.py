#Clase jugada
class Jugada:
    def __init__(self,numero,monto,dni):
        self.numero= numero
        self.monto = monto
        self.dni = dni
    
    def __str__(self):
        return f" monto: {self.monto}, dni: {self.dni}, Número: {self.numero}"
        
#Clase loteria
class Loteria:
    def __init__(self,numero_ganador):
        self.numero_ganador = numero_ganador
        
#Funcion verificar_ganador
    def verificar_ganador(self,jugadas):
        for jugada  in jugadas:
            num_str = str(jugada.numero)
            ganador_str = str(self.numero_ganador)

            # Comparar los dígitos finales
            coincidencias = 0
                
                # Verificar si el número jugado tiene los mismos últimos dígitos que el número ganador
            for i in range(1, min(len(num_str), len(ganador_str)) + 1):
                if num_str[-i] == ganador_str[-i]:
                        coincidencias += 1
                else:
                    break  
                    
            #coinicidencias:
            if coincidencias  == 1:
                pozo = jugada.monto * 7
                print(f"el ganador es la persona con dni:{jugada.dni}, con los numeros: {jugada.numero}")
                print(f"Coincidieron {coincidencias} dígitos. El pozo es: {pozo}")
            if coincidencias  == 2:
                pozo = jugada.monto * 70
                print(f"el ganador es la persona con dni:{jugada.dni}, con los numeros: {jugada.numero}")
                print(f"Coincidieron {coincidencias} dígitos. El pozo es: {pozo}")
            if coincidencias  == 3:
                pozo = jugada.monto * 700
                print(f"el ganador es la persona con dni:{jugada.dni}, con los numeros: {jugada.numero}")
                print(f"Coincidieron {coincidencias} dígitos. El pozo es: {pozo}")
                

#Cargar lista
jugadas=[
    Jugada(350, 500,"46213395"),
    Jugada(1012, 300,"11222333"),
    Jugada(51, 1500,"77765653")
]  

#Inicializo el numero ganador
Loteria = Loteria(350)

#Funcion a llamar
Loteria.verificar_ganador(jugadas);
