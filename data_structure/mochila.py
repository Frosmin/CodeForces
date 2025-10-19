capacidad  = 7
n = 5

lst = [[3,50],[2,40],[4,70],[5,80],[1,10]]


dp = [[0 for _ in range(capacidad + 1)] for _ in range(n + 1)]


for i in range(1,n+1):
    for k  in range(1,capacidad+1):
        capaci = k
        item = lst[i-1]
        peso = item[0]
        valor = item[1]
        if peso <= capaci:
            dp[i][k] = max(dp[i-1][k], valor + dp[i-1][k - peso])

        else:
            dp[i][k] = dp[i-1][k]
        



for i in range(n+1):    
    print(dp[i])

# valor de ganacia maxima es el ultimo de la matriz 
print(dp[n][capacidad])
