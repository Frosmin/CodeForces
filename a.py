linea = input()
n_intersecciones, m_calles, k_esfuerzo_max = map(int, linea.split())

grafo = [[] for _ in range(n_intersecciones + 1)]

for _ in range(m_calles):
            linea_calle = input()
            if not linea_calle:
                continue
            u, v, peso = map(int, linea_calle.split())
            grafo[u].append((v, peso))
            grafo[v].append((u, peso))

distancias = [float('inf')] * (n_intersecciones + 1)
distancias[1] = 0

visitados = [False] * (n_intersecciones + 1)

for _ in range(n_intersecciones):

        distancia_minima = float('inf')
        u = -1
        for i in range(1, n_intersecciones + 1):
            if not visitados[i] and distancias[i] < distancia_minima:
                distancia_minima = distancias[i]
                u = i

        if u == -1:
            break

        visitados[u] = True

        if u == n_intersecciones:
            break

        for v_vecino, peso_calle in grafo[u]:
            if not visitados[v_vecino] and distancias[u] + peso_calle < distancias[v_vecino]:
                distancias[v_vecino] = distancias[u] + peso_calle
                
if distancias[n_intersecciones] <= k_esfuerzo_max:
        print("SI")
else:
        print("NO")

