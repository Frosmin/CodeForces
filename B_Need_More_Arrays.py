
from bisect import bisect_right
 
 
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()[:n]))
    dp = [0] * n
    for i in range(n):
        if i == 0:
            mejor = 0
        else:
            mejor = dp[i-1]
        objetivo = a[i] - 2
        pos = bisect_right(a, objetivo, 0, i) - 1 
        if pos >= 0:
            mejor_con = 1 + dp[pos]
        else:
            mejor_con = 1 
        dp[i] = max(mejor, mejor_con)
    print(dp[n-1])