def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    k = int(input[ptr])
    ptr += 1

    INF = float('inf')


    C = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            C[i][j] = int(input[ptr])
            ptr += 1


    D = [row[:] for row in C]

    for k_node in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if D[i][j] > D[i][k_node] + D[k_node][j]:
                    D[i][j] = D[i][k_node] + D[k_node][j]

    q = int(input[ptr])
    ptr += 1

    for _ in range(q):
        s = int(input[ptr])
        ptr += 1
        t = int(input[ptr])
        ptr += 1
        nodes = list(range(1, k + 1)) + [s, t]
        edges = []
        m = len(nodes)
        for i in range(m):
            u = nodes[i]
            for j in range(i + 1, m):
                v = nodes[j]
                edges.append((D[u][v], u, v))

        edges.sort()

        parent = {}
        for node in nodes:
            parent[node] = node

        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u

        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                parent[root_v] = root_u

        total = 0
        count = 0
        for cost, u, v in edges:
            if find(u) != find(v):
                union(u, v)
                total += cost
                count += 1
                if count == m - 1:
                    break
        print(total)

if __name__ == '__main__':
    main()