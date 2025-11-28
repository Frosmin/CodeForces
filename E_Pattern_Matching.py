from sys import stdin
input=lambda :stdin.readline()[:-1]
 
def edgess(N,edges):
    M=len(edges)
    start=[0]*(N+1)
    elist=[0]*M
    for e in edges:
        start[e[0]+1]+=1
    for i in range(1,N+1):
        start[i]+=start[i-1]
    counter=start[:]
    for e in edges:
        elist[counter[e[0]]]=e[1]
        counter[e[0]]+=1
    visited=[]
    low=[0]*N
    Ord=[-1]*N
    ids=[0]*N
    NG=[0,0]
    def dfs(v):
        stack=[(v,-1,0),(v,-1,1)]
        while stack:
            v,bef,t=stack.pop()
            if t:
                if bef!=-1 and Ord[v]!=-1:
                    low[bef]=min(low[bef],Ord[v])
                    stack.pop()
                    continue
                low[v]=NG[0]
                Ord[v]=NG[0]
                NG[0]+=1
                visited.append(v)
                for i in range(start[v],start[v+1]):
                    to=elist[i]
                    if Ord[to]==-1:
                        stack.append((to,v,0))
                        stack.append((to,v,1))
                    else:
                        low[v]=min(low[v],Ord[to])
            else:
                if low[v]==Ord[v]:
                    while(True):
                        u=visited.pop()
                        Ord[u]=N
                        ids[u]=NG[1]
                        if u==v:
                            break
                    NG[1]+=1
                low[bef]=min(low[bef],low[v])
    for i in range(N):
        if Ord[i]==-1:
            dfs(i)
    for i in range(N):
        ids[i]=NG[1]-1-ids[i]
    group_num=NG[1]
    counts=[0]*group_num
    for x in ids:
        counts[x]+=1
    groups=[[] for i in range(group_num)]
    for i in range(N):
        groups[ids[i]].append(i)
    return groups
 
n,m,k=map(int,input().split())
def f(s):
  res=[]
  for i in s:
    if i=='_':
      res.append(-1)
    else:
      res.append(ord(i)-97)
  return res
 
def make(a):
  todo=[]
  for bit in range(1<<k):
    x=[]
    for i in range(k):
      if (bit>>i)&1:
        x.append(a[i])
      else:
        x.append(-1)
    todo.append(tuple(x))
  return todo
 
from collections import defaultdict
d=defaultdict(int)
for i in range(n):
  s=input()
  a=tuple(f(s))
  d[a]=i
 
memo={}
edges=[]
 
for _ in range(m):
  s,x=input().split()
  x=int(x)-1
  a=f(s)
  if tuple(a) in memo:
    if memo[tuple(a)]!=x:
      print('NO')
      exit()
    continue
  memo[tuple(a)]=x
  flag=False
  for b in make(a):
    if b in d:
      i=d[b]
      if i==x:
        flag=True
      else:
        edges.append((x,i))
  if not flag:
    print('NO')
    exit()
 
edgess=edgess(n,edges)
if len(edgess)==n:
  print('YES')
  print(*[i[0]+1 for i in edgess])
else:
  print('NO')