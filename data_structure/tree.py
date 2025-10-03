def bfs(inicio, grafo, n):
    visitado = [False] * (n + 1) #lista puro false 
    cola = []
    cola.append(inicio)
    visitado[inicio] = True

    while cola:
        nodo = cola.pop(0)  # sacar el primer elemento y lo imprime
        print(nodo, end=" ")

        for vecino in grafo[nodo]: # recore cada nodo y itera uno por una [1,2,3]
            if not visitado[vecino]:
                cola.append(vecino)
                visitado[vecino] = True
                
                
def dfs(nodo,visitados, grafo):
    
    visitado[nodo] = True
    print(nodo, end=" ")
    for vecino in grafo[nodo]:
        if not visitado[vecino]:
            dfs(vecino,visitado, grafo)



n = 6
aristas = [
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 5),
]

# Creamos una lista de listas (índice 0 no se usa)
grafo = [[] for _ in range(n + 1)]


# Llenamos la lista de adyacencia
for u, v in aristas:
    grafo[u].append(v)
    grafo[v].append(u)  # porque es no dirigido

# # Imprimimos la lista de adyacencia
# print(grafo)
# for i in range(1, n+1):
#     print(i, "->", grafo[i])


visitado  = [False] * (n+1)
dfs(1,visitado,grafo)

print(" ")
print("---------")

bfs(1,grafo,n)





