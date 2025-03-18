class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}
    
    def agregar_vertice(self, vertice):
        self.lista_adjacencia[vertice] = [] 
        
    def agregar_arista(self, vertice1, vertice2):
        self.lista_adjacencia[vertice1].append(vertice2)
        self.lista_adjacencia[vertice2].append(vertice1)
        
    
if __name__ == '__main__':
    grafo = Grafo()
    grafo.agregar_vertice('A')
    grafo.agregar_vertice('B')
    grafo.agregar_vertice('C')
    grafo.agregar_vertice('D')
    grafo.agregar_arista('A', 'B')
    grafo.agregar_arista('A', 'C')
    grafo.agregar_arista('B', 'C')
    print(grafo.lista_adjacencia)