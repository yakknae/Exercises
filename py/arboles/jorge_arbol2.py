class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1
    
    def __str__(self):
        return f"Nodo({self.valor})"

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
       if not self.raiz:
          self.raiz = Nodo(valor)
       else:
        self.raiz = self._agregar_recursivo(self.raiz, valor)
        

    # def agregar(self, valor):
    #     if not self.raiz:
    #         self.raiz = Nodo(valor)
    #     else:
    #         self.raiz = self._agregar_recursivo(self.raiz, valor)
            
    def _agregar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
               nodo.izq = self._agregar_recursivo(nodo.izq, valor)
        else:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
               nodo.der = self._agregar_recursivo(nodo.der, valor)
        
        # Actualizar altura del nodo actual
        self._actualizar_altura(nodo)

        # Verificar balanceo
        balance = self.factor_balanceo(nodo)

        #caso LL
        if balance > 1 and valor < nodo.izq.valor:
            return self.rotacion_der(nodo)
        
        #caso RR
        if balance < -1 and valor > nodo.der.valor:
            return self.rotacion_izq(nodo)
        
        #caso LR
        if balance > 1 and valor > nodo.izq.valor:
            nodo.izq = self.rotacion_izq(nodo.izq)
            return self.rotacion_der(nodo)
        
        #caso RL
        if balance < -1 and valor < nodo.der.valor:
            nodo.der = self.rotacion_der(nodo.der)
            return self.rotacion_izq(nodo)
        
        # Si no hubo rotación, devolvemos el nodo sin cambios
        return nodo
        
    #preorden
    def preorden(self, nodo): 
        if nodo:
            print(f'Valor del nodo: {nodo.valor} -> Factor de balanceo: {self.factor_balanceo(nodo)}')
            self.preorden(nodo.izq)
            self.preorden(nodo.der)

    #inorden
    def inorden(self,nodo):
        if nodo:
            self.inorden(nodo.izq)
            print(f'Valor del nodo: {nodo.valor} -> Factor de balanceo: {self.factor_balanceo(nodo)}')
            self.inorden(nodo.der)

    #postorden
    def postorden(self, nodo): 
        if nodo:
            self.postorden(nodo.izq)
            self.postorden(nodo.der)
            print(f'Valor del nodo: {nodo.valor} -> Factor de balanceo: {self.factor_balanceo(nodo)}')

    def _actualizar_altura(self, nodo):
        if nodo:
            nodo.altura = 1 + max(self.altura(nodo.izq), self.altura(nodo.der))

    def factor_balanceo(self, nodo):
        if not nodo:
            return 0
        return self.altura(nodo.izq) - self.altura(nodo.der)

    def altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura # Usa 0 si no tiene altura asignada

    def imprimir_alturas(self, nodo):
        if nodo:
            print(f"Nodo({nodo.valor}) -> Altura: {nodo.altura}")
            self.imprimir_alturas(nodo.izq)
            self.imprimir_alturas(nodo.der)

    def hojas(self):
        return self._hojas_recursivo(self.raiz)

    def _hojas_recursivo(self, nodo):
        if nodo is None:
            return []
        if nodo.izq is None and nodo.der is None:
            return [nodo.valor]
        return self._hojas_recursivo(nodo.izq) + self._hojas_recursivo(nodo.der)
    
    def rotacion_izq(self, z):
        y = z.der
        x = y.izq

        y.izq = z
        z.der = x

        self._actualizar_altura(z)
        self._actualizar_altura(y)

        return y

    def rotacion_der(self, z):
        y = z.izq
        x = y.der

        # Reconexion
        y.der = z
        z.izq = x

        # Actualizar alturas
        self._actualizar_altura(z)
        self._actualizar_altura(y)

        return y
    
    def buscar(self,dato):
        def _buscar_rec(nodo,valor,padre=None):
            """
            Parámetros:
            - nodo: el nodo actual donde estamos buscando.
            - valor: el valor que queremos encontrar.
            - padre: el nodo que está un nivel arriba (el 'padre' del nodo actual).
            """
            
            # PASO 1: Verifica si hay nodo
            if nodo is None:
                return None, None, None, None, None # nodo, padre, ubicacion, hijo_izq, hijo_der
            
            # PASO 2: ¿este el nodo que buscamos?
            if valor == nodo.valor:
                if padre is None:
                    # Si no tiene padre, entonces es la RAÍZ del árbol
                    ubicacion = "raiz"
                elif nodo == padre.izq:
                    # Si este nodo es el hijo izquierdo del padre
                    ubicacion = "izq"
                else:
                    # Si no es raíz ni izquierdo, entonces es el derecho
                    ubicacion = "der"

                # vamos a ver quiénes son sus hijos (si existen)
                # Hijo izquierdo
                if nodo.izq is not None:
                    # Si existe un nodo a la izquierda, guardamos su valor
                    hijo_izq = nodo.izq.valor
                else:
                    hijo_izq = None

                # Hijo derecho
                if nodo.der is not None:
                    hijo_der = nodo.der.valor
                else: 
                    hijo_der = None

                # Devolvemos toda la información útil
                return nodo, padre, ubicacion, hijo_izq, hijo_der
            
            # Paso 3: Aún no lo encontramos.
            elif valor < nodo.valor:
                # El valor que buscamos es MENOR que el del nodo actual
                return _buscar_rec(nodo.izq,valor,nodo)
            else:
                # El valor que buscamos es MAYOR que el del nodo actual
                return _buscar_rec(nodo.der, valor,nodo)
            
        # Iniciamos la búsqueda desde la RAÍZ del árbol
        # Empezamos con 'padre = None' porque la raíz no tiene padre
        return _buscar_rec(self.raiz,dato)

        





print("Ejercicio 1: Implementación de un árbol binario")
arbol = ArbolBinario()
valores = [1, 2, 3, 4]

for v in valores:
    arbol.agregar(v)
    print("-")

print(f"raiz: {arbol.raiz}")
print(f"raiz.izq: {arbol.raiz.izq}")
print(f"raiz.der: {arbol.raiz.der}")
print(f"raiz.der.der: {arbol.raiz.der.der}")

print("Factor de balanceo del nodo raíz:", arbol.factor_balanceo(arbol.raiz))
print("Altura del árbol:", arbol.altura(arbol.raiz))    
print("Hojas del árbol:", arbol.hojas())

print("\nAlturas de los nodos:")
arbol.imprimir_alturas(arbol.raiz)

print("\nRecorrido preorden:")
arbol.preorden(arbol.raiz)
print("\nRecorrido postorden:")
arbol.postorden(arbol.raiz)
print("\nRecorrido Inorden:")
arbol.inorden(arbol.raiz)

nodo, padre, ubicacion, h_izq, h_der = arbol.buscar(3)
if nodo:
    print(f"✅ Encontrado: {nodo.valor}")
    print(f"🔹 Padre: {padre.valor if padre else 'Ninguno (es raíz)'}")
    print(f"🔹 Ubicación: {ubicacion}")
    print(f"🔹 Hijo izquierdo: {h_izq}")
    print(f"🔹 Hijo derecho: {h_der}")
else:
    print("❌ No encontrado")
