


# import sys
# import heapq


# input = sys.stdin.readline
# t = int(input())
# res = []
# for _ in range(t):
#     n = int(input())
#     lista = list(map(int, input().split()))
#     izq = [(i - 1 + n) % n for i in range(n)]
#     der = [(i + 1) % n for i in range(n)]
#     vivo = [True] * n
#     pq = []
#     u = 0
#     for i in range(n):
#         j = der[i]
#         heapq.heappush(pq, (max(lista[i], lista[j]), u, i, j))
#         u += 1
#     total = 0
#     merges = 0
#     while merges < n - 1:
#         cost, _, u, v = heapq.heappop(pq)
#         if not (vivo[u] and vivo[v]):
#             continue
#         if der[u] != v:
#             continue
#         total += cost
#         merges += 1
#         if lista[u] <= lista[v]:
#             izq_u = izq[u]
#             vivo[u] = False
#             izq[v] = izq_u
#             der[izq_u] = v
#             if merges < n - 1 and izq_u != v:
#                 heapq.heappush(pq, (max(lista[izq_u], lista[v]), u, izq_u, v))
#                 u += 1
#         else:
#             der_v = der[v]
#             vivo[v] = False
#             der[u] = der_v
#             izq[der_v] = u
#             if merges < n - 1 and der_v != u:
#                 heapq.heappush(pq, (max(lista[u], lista[der_v]), u, u, der_v))
#                 u += 1
#     res.append(str(total))
# print("\n".join(res))


import sys

input = sys.stdin.readline
t = int(input())
res = []
for _ in range(t):
    n = int(input())
    lsita = list(map(int, input().split()))
    izq = [(i - 1) % n for i in range(n)]
    der = [(i + 1) % n for i in range(n)]
    order = sorted(range(n), key=lambda i: (lsita[i], i))
    total = 0
    for idx in order[:n - 1]:
        l = izq[idx]
        r = der[idx]
        total += min(lsita[l], lsita[r])
        der[l] = r
        izq[r] = l
    res.append(str(total))
sys.stdout.write("\n".join(res))

