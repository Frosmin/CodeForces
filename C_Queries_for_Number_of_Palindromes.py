import sys
input = lambda: sys.stdin.readline().rstrip()
 
s = input()
n = len(s)
 
dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][i] = 1
    if i and s[i - 1] == s[i - 2]:
        dp[i - 1][i] = 1
for i in range(2, n):
    for j in range(1, n - i + 1):
        if s[j - 1] == s[j + i - 1] and dp[j + 1][j + i - 1]:
            dp[j][j + i] = 1
            
            
for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] += dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
 
for _ in range(int(input())):
    l, r = map(int, input().split())
    ans = dp[r][r] - dp[r][l - 1] - dp[l - 1][r] + dp[l - 1][l - 1]
    print(ans)