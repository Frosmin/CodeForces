# Python 3
import sys
from bisect import bisect_right

input = sys.stdin.readline


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))
    dp = [0] * n
    for i in range(n):
        if i == 0:
            best_without = 0
        else:
            best_without = dp[i-1]
        target = a[i] - 2
        pos = bisect_right(a, target, 0, i) - 1 
        if pos >= 0:
            best_with = 1 + dp[pos]
        else:
            best_with = 1 
        dp[i] = max(best_without, best_with)
    print(dp[n-1])


