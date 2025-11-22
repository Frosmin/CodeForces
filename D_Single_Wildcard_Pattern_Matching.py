import heapq
import sys, os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
def grafo(n, m):
    x, y, s = [0] * (2 * m), [0] * m, [0] * (n + 3)
    for i in range(0, 2 * m, 2):
        u, v, w = map(int, input().split())
        s[u + 2] += 1
        x[i], x[i + 1] = u, v
        y[i >> 1] = w
    for i in range(3, n + 3):
        s[i] += s[i - 1]
    G, W = [0] * m, [0] * m
    for i in range(0, 2 * m, 2):
        j = x[i] + 1
        G[s[j]] = x[i ^ 1]
        W[s[j]] = y[i >> 1]
        s[j] += 1
    return G, W, s
 
def f(i):
    if not lazy[i]:
        return
    tree[i] += lazy[i]
    if i < l1:
        lazy[i << 1] += lazy[i]
        lazy[i << 1 ^ 1] += lazy[i]
    lazy[i] = 0
    return
 
def actualizar(l, r, s):
    q, ll, rr, i = [1], [0], [l1 - 1], 0
    while len(q) ^ i:
        j = q[i]
        l0, r0 = ll[i], rr[i]
        if l <= l0 and r0 <= r:
            if s:
                lazy[j] += s
            f(j)
            i += 1
            continue
        f(j)
        m0 = (l0 + r0) >> 1
        if l <= m0 and l0 <= r:
            q.append(j << 1)
            ll.append(l0)
            rr.append(m0)
        if l <= r0 and m0 + 1 <= r:
            q.append(j << 1 ^ 1)
            ll.append(m0 + 1)
            rr.append(r0)
        i += 1
    for i in q[::-1]:
        if i < l1:
            j, k = i << 1, i << 1 ^ 1
            f(j)
            f(k)
            tree[i] = min(tree[j], tree[k])
    return
 
def get_min(s, t):
    actualizar(s, t, 0)
    s += l1
    t += l1
    res = inf
    while s <= t:
        if s % 2:
            res = min(res, tree[s])
            s += 1
        s >>= 1
        if not t % 2:
            res = min(res, tree[t])
            t -= 1
        t >>= 1
    return res
 
n, m, q = map(int, input().split())
a, b = [0] * (n + 1), [0] * n
for i in range(1, n):
    x, y = map(int, input().split())
    a[i], b[i] = x, y
G, W, s0 = grafo(n, m)
l1 = pow(2, (n + 1).bit_length())
l2 = 2 * l1
inf = pow(10, 15) + 1
tree, lazy = [inf] * l2, [0] * l2
mi = inf
for i in range(n - 1, -1, -1):
    mi = min(mi, b[i])
    tree[i + l1] = mi
for i in range(l1 - 1, 0, -1):
    tree[i] = min(tree[2 * i], tree[2 * i + 1])
c = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(s0[i], s0[i + 1]):
        actualizar(0, G[j] - 1, W[j])
    c[i] = tree[1]
h = []
for i in range(1, n + 1):
    heapq.heappush(h, (a[i] + c[i], i))
res = [h[0][0]]
for _ in range(q):
    v, w = map(int, input().split())
    heapq.heappush(h, (w + c[v], v))
    a[v] = w
    while (a[h[0][1]] + c[h[0][1]]) ^ h[0][0]:
        heapq.heappop(h)
    res0 = h[0][0]
    res.append(res0)
sys.stdout.write("\n".join(map(str, res)))