for _ in range(int(input())):
        n,m = [int(t) for t in input().split()]
        arr = [int(t) for t in input().split()]
 
        intvs = [[int(t) for t in input().split()] for _ in range(m)]
        for e in intvs: e[0] -= 1
        for i in range(n): intvs.append( (i,i+1) )
        
        limiar = []
        s = -1
        for l,r in sorted(intvs,key=lambda x: (x[0],-x[1])):
                if r > s:
                        s = r
                        limiar.append((l,r))
        mv = [-1]*(n+1)
        for j in range(len(limiar)-1):
                l = limiar[j+1][0]
                r = limiar[j][1]
                mv[l] = r
        mv[n] = n
 
        dp = [[-1]*(n+1) for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(n+1):
                t = mv[i]
                if t > -1:
                        for b in range(n+1):
                                s = dp[i][b]
                                if s == -1: continue
                                dp[t][s] = max(dp[t][s],b)
                if i == n: break
                for b in range(n+1):
                        s = dp[i][b]
                        if s == -1: continue
                        dp[i+1][b] = max(dp[i+1][b],s+1)
        
        v = dp[n]
        for i in range(n-1,-1,-1): v[i] = max(v[i],v[i+1])
        
        cnt = [0]*(n+2)
        for e in arr: cnt[e] += 1
 
        grande = n
        punto = 0
        peque = 0
        res2 = []
        for i in range(1,n+1):
                grande -= cnt[i]
                punto += cnt[i]
                punto -= cnt[i-1]
                peque += cnt[i-1]
                res2.append( "1" if peque <= v[grande] else "0" )
        print( "".join(res2) )