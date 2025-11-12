
def escaleras(n):
    if n == 1 :
        return 1
    elif n ==2:
        return 2
    else:
        return escaleras(n-1) + escaleras(n-2)
    
n = 35
# print(escaleras(n))

dp = [0] * (n+1)
dp[1] = 1
dp[2] = 2

for i in range(3,n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[-1])


