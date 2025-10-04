import sys; R = sys.stdin.readline
S = lambda: map(int,R().split())
from collections import deque
 
def f(x):
    global s
    u = p[x]//2==p[g[x]]
    if u!=c[x]: c[x] = u; s += 2*u-1
for _ in range(int(R())):
    n,q = S()
    e = [[] for _ in range(n+1)]
    S()
    p = [0]+[*S()]
    Q = deque([1])
    j = (n+1)//2
    g = [0]*(n+1)
    while j>1:
        for _ in range(len(Q)):
            u = Q.popleft()
            g[u+1] = u
            g[u+j] = u
            e[u] += u+1,
            e[u] += u+j,
            Q += u+1,
            Q += u+j,
        j //= 2
    c = [0]+[p[i]//2==p[g[i]] for i in range(1,n+1)]
    s = sum(c)
    for _ in range(q):
        x,y = S()
        p[x],p[y] = p[y],p[x]
        f(x); f(y)
        for z in e[x]: f(z)
        for z in e[y]: f(z)
        print(('NO','YES')[s==n])