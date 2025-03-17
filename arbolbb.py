class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBB:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
            return
        
        self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecha, valor)
        # Si el valor ya existe, no hacemos nada
    
    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)
    
    def _buscar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None:
            return False
        
        if nodo_actual.valor == valor:
            return True
        
        if valor < nodo_actual.valor:
            return self._buscar_recursivo(nodo_actual.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo_actual.derecha, valor)
    
    def recorrido_inorden(self):
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _inorden_recursivo(self, nodo, resultado):
        if nodo:
            self._inorden_recursivo(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self._inorden_recursivo(nodo.derecha, resultado)
    
    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)
    
    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return None
        
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, valor)
        else:
            # Caso 1: Nodo hoja (sin hijos)
            if nodo.izquierda is None and nodo.derecha is None:
                return None
            
            # Caso 2: Nodo con un hijo
            elif nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            
            # Caso 3: Nodo con dos hijos
            # Encontrar el sucesor inorden (mínimo del subárbol derecho