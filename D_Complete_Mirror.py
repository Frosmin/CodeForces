from collections import deque
def res():
  def check(x):
    vis = [0]*(n+1)
    vis[x] = 1
    ddeg = [-1]*(n)
    s = [(0,x)]
    while s:
      d,x = s.pop()
      for v in g[x]:
        if vis[v]: continue
        vis[v]=1
        if ddeg[d+1]==-1:
          ddeg[d+1] = deg[v]
        elif ddeg[d+1]!=deg[v]:
          return 0
        s.append((d+1, v))
    return 1
  def dist(x):
    vis = [0]*(n+1)
    vis[x] = 1
    d = [0]*(n+1)
    s = [x]
    mx = x
    while s:
      x = s.pop()
      for v in g[x]:
        if vis[v]: continue
        vis[v]=1
        d[v] = d[x]+1
        if d[v]>d[mx]: mx=v
        s.append(v)
    return mx, d
  n = int(input())
  g = [[] for i in range(n+1)]
  deg = [0]*(n+1)
  for i in range(n-1):
    u,v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
    deg[u]+=1
    deg[v]+=1
  if n<3:
    return 1
  a,d1 = dist(1)
  b,da = dist(a)
  v,db = dist(b)
  if check(a): return a
  if check(b): return b
  x = -1
  for i in range(1, n+1):
    if da[i]+db[i] == da[b] and da[i]==db[i]: x = i
  if x==-1: return -1
  if check(x): return x
  s = deque([x])
  vis = [0]*(n+1)
  vis[x]=1
  dd = [-1]*2
  while s:
    x = s.popleft()
    for v in g[x]:
      if vis[v]: continue
      vis[v]=1
      if deg[v]==1:
        dd[1] = v
        if dd[0]==-1:
          dd[0] = v
      s.append(v)
  for x in dd:
    if check(x): return x
  return -1
 
print(res())