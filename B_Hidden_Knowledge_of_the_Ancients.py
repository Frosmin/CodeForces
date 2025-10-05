import random
RANDOM = random.randrange(2**62)
 
def wrap(x):
  return x ^ RANDOM
 
for _ in range(int(input())):
    n,k,l,r=map(int,input().split())
    a=list(map(int,input().split()))
    ans=0
    f={}
    g={}
    x1=x2=0
    for i in range(n):
        x=a[i]
        f[wrap(x)]=f.get(wrap(x),0)+1
        while len(f)>k:
            f[wrap(a[x1])]-=1
            if f[wrap(a[x1])]==0: del f[wrap(a[x1])]
            x1+=1
        g[wrap(x)]=g.get(wrap(x),0)+1
        while len(g)>=k:
            g[wrap(a[x2])]-=1
            if g[wrap(a[x2])]==0: del g[wrap(a[x2])]
            x2+=1
        ans+=max(0,min(x2-1,i-l+1)-max(x1,i-r+1)+1)
    print(ans)