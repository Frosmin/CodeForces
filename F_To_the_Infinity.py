import sys
import random
import time
import heapq

MAXN = 400005

class Node:
    def __init__(self):
        self.l = 0
        self.r = 0
        self.h = 0

def solve():
    n = int(input())
    
    h = [0] * (n + 1)
    tr = [Node() for _ in range(n * 50 + 5)]
    rt = [0] * (n + 1)
    d = [0] * (n + 1)
    ls = [0] * (n + 1)
    rs = [0] * (n + 1)
    fa = [0] * (n + 1)
    rv = [0] * (n + 1)
    cnt = 0
    
    for i in range(1, n + 1):
        h[i] = random.randint(0, 2**64 - 1)
    
    def update(rt_idx, l, r, x):
        nonlocal cnt
        if rt_idx == 0:
            cnt += 1
            rt_idx = cnt
            tr[rt_idx].l = tr[rt_idx].r = tr[rt_idx].h = 0
        
        tr[rt_idx].h += h[x]
        if l == r:
            return rt_idx
        
        mid = (l + r) >> 1
        if x <= mid:
            tr[rt_idx].l = update(tr[rt_idx].l, l, mid, x)
        else:
            tr[rt_idx].r = update(tr[rt_idx].r, mid + 1, r, x)
        
        return rt_idx
    
    def dfs(u):
        if ls[u] == 0:
            d[u] = 0
        else:
            dfs(ls[u])
            dfs(rs[u])
            fa[ls[u]] = fa[rs[u]] = u
            d[u] = 2
    
    class Key:
        def __init__(self, idx):
            self.idx = idx
        
        def __lt__(self, other):
            x, y = self.idx, other.idx
            r1, r2 = rt[x], rt[y]
            
            if tr[r1].h == tr[r2].h:
                return x < y
            
            l, r = 1, n
            while l < r:
                mid = (l + r) >> 1
                if tr[tr[r1].r].h == tr[tr[r2].r].h:
                    r1, r2 = tr[r1].l, tr[r2].l
                    r = mid
                else:
                    r1, r2 = tr[r1].r, tr[r2].r
                    l = mid + 1
            
            return tr[r1].h < tr[r2].h
    
    for i in range(1, n + 1):
        ls[i], rs[i] = map(int, input().split())
        fa[i] = 0
        rt[i] = 0
        rv[i] = 0
    
    dfs(1)
    
    pq = []
    for i in range(1, n + 1):
        if d[i] == 0:
            heapq.heappush(pq, Key(i))
    
    tot = 0
    lh = float('inf')
    result = []
    
    while pq:
        u = heapq.heappop(pq).idx
        if tr[rt[u]].h != lh:
            lh = tr[rt[u]].h
            tot += 1
        
        rv[u] = tot
        result.append(str(u))
        
        v = fa[u]
        if v:
            d[v] -= 1
            if d[v] == 0:
                rt[v] = rt[ls[v]]
                rt[ls[v]] = 0
                rt[v] = update(rt[v], 1, n, rv[rs[v]])
                heapq.heappush(pq, Key(v))
    
    print(" ".join(result))

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()