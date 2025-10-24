# def fact(n):
#     if(n<1):
#         return 1
#     return n * fact(n-1)
    
# n = int(input())
# prod = 1
# sum = 0
# for i in range(n):
#     k = int(input())
#     prod *= fact(sum+k-1)//fact(sum)//fact(k-1)
#     prod = prod % 1000000007
#     sum += k
# print(int(prod))



# res,s=1,0
# for _ in range(int(input())):
# 	n=int(input())
# 	s+=n
# 	if s==n:continue
# 	k=1
# 	for i in range(1,n):
# 		k=k*(s-i)//i
# 	res=(res*k)%(10**9+7)
# print(res)



 
n, k = list(map(int, input().split()))
mod = 998244353
if k == 1:
    print(2)
else:
    dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n + 1)]
    dp[1][1] =[2, 0]
    dp[1][2] = [0, 2]
    for i in range(2, n + 1):
        dp[i][1][0] = (dp[i - 1][0][0] + dp[i - 1][1][0] + dp[i - 1][1][1] * 2) % mod
        dp[i][1][1] = (dp[i - 1][0][0] * 2 + dp[i - 1][1][1]) % mod
        for j in range(2, min(2 * i, k) + 1):
            dp[i][j][0] = (dp[i - 1][j - 1][0] + dp[i - 1][j][0] + dp[i - 1][j][1] * 2) % mod
            dp[i][j][1] = (dp[i - 1][j - 2][1] + dp[i - 1][j - 1][0] * 2 + dp[i - 1][j][1]) % mod
    print(sum(dp[n][k]) % mod)