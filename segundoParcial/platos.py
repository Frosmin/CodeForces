# import sys
# from collections import deque

# class Dinic:
#     def __init__(self, n):
#         self.n = n
#         self.g = [[] for _ in range(n)]
#         self.level = [0] * n
#         self.it = [0] * n

#     def add_edge(self, u, v, cap):
#         self.g[u].append([v, cap, len(self.g[v])])
#         self.g[v].append([u, 0, len(self.g[u]) - 1])

#     def bfs(self, s, t):
#         self.level = [-1] * self.n
#         q = deque([s])
#         self.level[s] = 0
#         while q:
#             u = q.popleft()
#             for v, cap, rev in self.g[u]:
#                 if cap > 0 and self.level[v] < 0:
#                     self.level[v] = self.level[u] + 1
#                     q.append(v)
#         return self.level[t] >= 0

#     def dfs(self, u, t, f):
#         if u == t:
#             return f
#         for i in range(self.it[u], len(self.g[u])):
#             self.it[u] = i
#             v, cap, rev = self.g[u][i]
#             if cap > 0 and self.level[v] == self.level[u] + 1:
#                 pushed = self.dfs(v, t, min(f, cap))
#                 if pushed:
                    
#                     self.g[u][i][1] -= pushed
                    
#                     self.g[v][rev][1] += pushed
#                     return pushed
#         return 0

#     def max_flow(self, s, t):
#         flow = 0
#         INF = 10**9
#         while self.bfs(s, t):
#             self.it = [0] * self.n
#             while True:
#                 pushed = self.dfs(s, t, INF)
#                 if pushed == 0:
#                     break
#                 flow += pushed
#         return flow

# def main():
#     data = list(map(int, sys.stdin.read().strip().split()))
#     if not data:
#         return
#     idx = 0
#     n = data[idx]; idx += 1  
#     m = data[idx]; idx += 1  

#     c = data[idx:idx+n]; idx += n  


#     S = 0
#     T = m + n + 1
#     N = T + 1

#     dinic = Dinic(N)

    
#     for cust in range(1, m + 1):
#         dinic.add_edge(S, cust, 1)

    
#     for j in range(1, n + 1):
#         dish_node = m + j
#         dinic.add_edge(dish_node, T, c[j - 1])


#     for cust in range(1, m + 1):
#         if idx >= len(data):
#             break
#         k = data[idx]; idx += 1
#         for _ in range(k):
#             dish_id = data[idx]; idx += 1  
#             dish_node = m + dish_id
#             dinic.add_edge(cust, dish_node, 1)

#     ans = dinic.max_flow(S, T)
#     print(ans)

# if __name__ == "__main__":
#     main()

# import sys

# def solucion():
#     data = list(map(int, sys.stdin.read().strip().split()))
#     idx = 0
#     n = data[idx]; idx += 1  # platos
#     m = data[idx]; idx += 1  # clientes
#     c = data[idx:idx+n]; idx += n  # capacidades por plato

#     # Prefijos para asignar índices a copias de platos
#     base = [0]*n
#     total = 0
#     for i in range(n):
#         base[i] = total
#         total += c[i]  # total nodos lado derecho (copias)

    
#     adj = [[] for _ in range(m)]
#     for cliente in range(m):
#         k = data[idx]; idx += 1
#         for _ in range(k):
#             dish = data[idx] - 1; idx += 1  # a 0-based
#             start = base[dish]
#             end = start + c[dish]
#             # Añadimos todas las copias disponibles de ese plato
#             adj[cliente].extend(range(start, end))

#     matchR = [-1] * total  # match para cada copia de plato

#     sys.setrecursionlimit(1000000)

#     def dfs(u, seen):
#         for v in adj[u]:
#             if not seen[v]:
#                 seen[v] = True
#                 if matchR[v] == -1 or dfs(matchR[v], seen):
#                     matchR[v] = u
#                     return True
#         return False

    
#     res = 0
#     for u in range(m):
#         seen = [False]*total
#         if dfs(u, seen):
            
#             res += 1

#     print(
#         res
#     )

# solucion()


from collections import deque

def bfs(cap, ini, sin, papa):
    visitados = [False] * len(cap)
    cola = deque([ini])
    visitados[ini] = True
    while cola:
        u = cola.popleft()
        for v in range(len(cap)):
            if not visitados[v] and cap[u][v] > 0:
                visitados[v] = True
                papa[v] = u
                if v == sin:
                    return True
                cola.append(v)
    return False

def karp(cap, ini, sin):
    papa = [-1] * len(cap)
    max_flow = 0
    while bfs(cap, ini, sin, papa):
        path_flow = float('Inf')
        s = sin
        while s != ini:
            path_flow = min(path_flow, cap[papa[s]][s])
            s = papa[s]
        max_flow += path_flow
        v = sin
        while v != ini:
            u = papa[v]
            cap[u][v] -= path_flow
            cap[v][u] += path_flow
            v = papa[v]
    return max_flow

def main():
    import sys
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    capa = list(map(int, data[idx:idx + n])); idx += n
    
    total_nodos = 1 + m + n + 1
    cap_matrix = [[0] * total_nodos for _ in range(total_nodos)]
    
    ini = 0
    sin = total_nodos - 1
    
    for i in range(1, m + 1):
        cap_matrix[ini][i] = 1
    
    for i in range(1, m + 1):
        k = int(data[idx]); idx += 1
        for _ in range(k):
            dish = int(data[idx]); idx += 1
            cap_matrix[i][m + dish] = 1
    
    for dish in range(1, n + 1):
         cap_matrix[m + dish][sin] = capa[dish - 1]
    
    max_flow = karp(cap_matrix, ini, sin)
    print(max_flow)

if __name__ == "__main__":
    main()