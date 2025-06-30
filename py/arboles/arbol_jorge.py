class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

 #   def agregar(self, valor):
 #       if not self.raiz:
 #          self.raiz = Nodo(valor)
 #       else:
 #        self.raiz = self._agregar_recursivo(self.raiz, valor)
 #      self.preorden(self.raiz)

    def agregar(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self.raiz = self._agregar_recursivo(self.raiz, valor)
            
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
            nodo.der = self.rotacion_der(nodo.der)
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
            self.preorden(nodo.izq)
            self.preorden(nodo.der)
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
        return getattr(nodo, 'altura', 0)  # Usa 0 si no tiene altura asignada


    def hojas(self):
        return self._hojas_recursivo(self.raiz)

    def _hojas_recursivo(self, nodo):
        if nodo is None:
            return []
        if nodo.izq is None and nodo.der is None:
            return [nodo.valor]
        return self._hojas_recursivo(nodo.izq) + self._hojas_recursivo(nodo.der)
    
    def rotacion_izq(self,z):
        y = z.der # y es el hijo derecho de z
        x = y.der # x es el hijo derecho de y
        # Paso 1: Movemos x como hijo izquierdo de z (T2)
        z.der = x
        # Paso 2: y ahora apunta a z como su hijo izquierdo
        y.izq = z

        # Actualizamos alturas desde abajo hacia arriba
        self._actualizar_altura(z)
        self._actualizar_altura(y)

        # Devolvemos la nueva raíz del subárbol
        return y


    def rotacion_der(self,z):
        y  = z.izq
        x = y.izq
        z.izq = x
        y.der = z
        self._actualizar_altura(z)
        self._actualizar_altura(y)
        return y


print("Ejercicio 1: Implementación de un árbol binario")
arbol = ArbolBinario()
valores = [1, 6, 3]

for v in valores:
    arbol.agregar(v)
    print("-")


print("Factor de balanceo del nodo raíz:", arbol.factor_balanceo(arbol.raiz))
print("Altura del árbol:", arbol.altura(arbol.raiz))    
print("Hojas del árbol:", arbol.hojas())