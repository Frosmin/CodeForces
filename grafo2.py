# class Grafo:
#     def __init__(self):
#         self.lista_adjacencia = {}
    
#     def agregar_vertice(self, vertice):
#         self.lista_adjacencia[vertice] = [] 
        
#     def agregar_arista(self, vertice1, vertice2):
#         self.lista_adjacencia[vertice1].append(vertice2)
#         self.lista_adjacencia[vertice2].append(vertice1)
        
    
# if __name__ == '__main__':
#     grafo = Grafo()
#     grafo.agregar_vertice('A')
#     grafo.agregar_vertice('B')
#     grafo.agregar_vertice('C')
#     grafo.agregar_vertice('D')
#     grafo.agregar_arista('A', 'B')
#     grafo.agregar_arista('A', 'C')
#     grafo.agregar_arista('B', 'C')
#     print(grafo.lista_adjacencia)



def crear_grafo(n, aristas, dirigido=False):
    """
    Crea un grafo con n vértices (0 a n-1)
    aristas: lista de tuplas (u, v) o (u, v, peso)
    """
    grafo = [[] for _ in range(n)]
    
    for arista in aristas:
        if len(arista) == 2:  # Sin peso
            u, v = arista
            grafo[u].append(v)
            if not dirigido:
                grafo[v].append(u)
        else:  # Con peso
            u, v, peso = arista
            grafo[u].append((v, peso))
            if not dirigido:
                grafo[v].append((u, peso))
    
    return grafo

# Ejemplo de uso
if __name__ == "__main__":
    n = 4  # número de vértices (0, 1, 2, 3)
    
    # Lista de aristas (u, v)
    aristas = [(0, 1), (0, 2), (1, 2)]
    
    grafo = crear_grafo(n, aristas)
    print("Grafo no dirigido:")
    for i in range(n):
        print(f"{i}: {grafo[i]}")
    
    # Grafo dirigido
    grafo_dir = crear_grafo(n, aristas, dirigido=True)
    print("\nGrafo dirigido:")
    for i in range(n):
        print(f"{i}: {grafo_dir[i]}")
    
    # Grafo ponderado
    aristas_peso = [(0, 1, 5), (0, 2, 3), (1, 2, 2)]
    grafo_peso = crear_grafo(n, aristas_peso)
    print("\nGrafo ponderado:")
    for i in range(n):
        print(f"{i}: {grafo_peso[i]}")