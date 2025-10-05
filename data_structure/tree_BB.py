n = 5
adj = [[] for _ in range(n + 1)]  # lista de adyacencia
print(adj)

# Agregar aristas (bidireccional)
edges = [(1,2), (1,3), (2,4), (2,5)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

# Mostrar conexiones
for i in range(1, n+1):
    print(f"Nodo {i}:", adj[i])





