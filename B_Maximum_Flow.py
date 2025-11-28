import sys
from collections import deque
 

def add(u, v, w):
    global tot
    ver[tot] = v
    edge[tot] = w
    nex[tot] = head[u]
    head[u] = tot
    tot += 1
 
    ver[tot] = u
    edge[tot] = 0
    nex[tot] = head[v]
    head[v] = tot
    tot += 1
 

def bfs():
    global dep
    dep = [0] * (n + 2)
    q = deque()
    q.append(s)
    dep[s] = 1
 
    while q:
        x = q.popleft()
        i = head[x]
        while i:
            if edge[i] and not dep[ver[i]]:
                q.append(ver[i])
                dep[ver[i]] = dep[x] + 1
                if ver[i] == t:
                    return True
            i = nex[i]
    return False
 

def dinic(x, flow):
    if x == t:
        return flow
 
    rest = flow
    i = now[x]
 
    while i and rest:
        now[x] = i
        if edge[i] and dep[ver[i]] == dep[x] + 1:
            k = dinic(ver[i], min(edge[i], rest))
            if not k:
                dep[ver[i]] = 0
            rest -= k
            edge[i] -= k
            edge[i ^ 1] += k
        i = nex[i]
 
    return flow - rest

def dfs(x):
    vis[x] = 1
    i = head[x]
    while i:
        if not vis[ver[i]] and edge[i]:
            dfs(ver[i])
        i = nex[i]
 
if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
 
   
    n = int(data[0])
    m = int(data[1])
    s = int(data[2])
    t = int(data[3])
 
    tot = 2  
    maxflow = 0
    flow = 0
 

    es = [0] * (m + 1)
    a = [0] * (m + 1)
    b = [0] * (m + 1)
    g = [0] * (m + 1)
 
    vis = [0] * (n + 2)
    dep = [0] * (n + 2)
    head = [0] * (n + 2)
    now = [0] * (n + 2)
 
    ver = [0] * (30001)
    edge = [0] * (30001)
    nex = [0] * (30001)
 
    idx = 4
    for i in range(1, m + 1):
        a[i] = int(data[idx])
        b[i] = int(data[idx + 1])
        g[i] = int(data[idx + 2])
        idx += 3
        if g[i]:
            add(a[i], b[i], 1)
            add(b[i], a[i], int(1e6))
        else:
            add(a[i], b[i], int(1e6))
 

    while bfs():
        for i in range(1, n + 1):
            now[i] = head[i]
        while True:
            flow = dinic(s, int(1e6))
            if not flow:
                break
            maxflow += flow
 
    dfs(s) 
    print(maxflow)
 

    for i in range(1, n + 1):
        head[i] = 0
 
    maxflow = 0
    tot = 2
    add(t, s, int(1e6))
    s, t = 0, n + 1
 
    for i in range(1, m + 1):
        if g[i]:
            add(a[i], b[i], int(1e6 - 1))
            add(s, b[i], 1)
            add(a[i], t, 1)
            es[i] = tot - 4
 

    while bfs():
        for i in range(n + 2):
            now[i] = head[i]
        while True:
            flow = dinic(s, int(1e6))
            if not flow:
                break
            maxflow += flow
 

    for i in range(1, m + 1):
        if g[i]:
            if vis[a[i]] != vis[b[i]]:
                print(edge[es[i]] + 1, edge[es[i]] + 1)
            else:
                print(edge[es[i]] + 1, 1000000)
        else:
            print(0, 1000000)