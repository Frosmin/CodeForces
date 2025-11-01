inf=1<<20
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()[:n]))
    dp=[0]*(n+1)
    dp[-2]=1
    for i in range(n-2,-1,-1):
        dp[i]=min(1+dp[i+1],dp[i+a[i]+1] if i+a[i]+1<=n else inf)
    print(dp[0])