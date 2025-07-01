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




print("Ejercicio 1: Implementación de un árbol binario")
arbol = ArbolBinario()
valores = [1, 2, 3, 4]

for v in valores:
    arbol.agregar(v)
    print("-")

print(f"raiz.raiz: {arbol.raiz}")
print(f"raiz.izq: {arbol.raiz.izq}")
print(f"raiz.der: {arbol.raiz.der}")
print(f"raiz.der.der: {arbol.raiz.der.der}")

print("Factor de balanceo del nodo raíz:", arbol.factor_balanceo(arbol.raiz))
print("Altura del árbol:", arbol.altura(arbol.raiz))    
print("Hojas del árbol:", arbol.hojas())

print("\nRecorrido preorden:")
arbol.preorden(arbol.raiz)
print("\nRecorrido postorden:")
arbol.postorden(arbol.raiz)
print("\nRecorrido Inorden:")
arbol.inorden(arbol.raiz)