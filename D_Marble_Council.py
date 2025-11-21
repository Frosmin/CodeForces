from collections import Counter

MOD = 998244353
MAX_N = 5000
INV = [0] * (MAX_N + 1)
INV[1] = 1
for i in range(2, MAX_N + 1):
    INV[i] = MOD - (MOD // i) * INV[MOD % i] % MOD

res = []
for _ in range(int(input())):
    n = int(input())
    lista = list(map(int,input().split()))
    freq = Counter(lista)
    counts = sorted(freq.values())
    proba = 1
    for c in counts:
        proba = (proba * c) % MOD
    dp = [0] * (n + 1)
    dp[0] = 1
    suma = 1
    for c in counts:
        limite = n - 2 * c
        if limite >= 0:
            pre = 0
            for s in range(limite + 1):
                pre += dp[s]
                if pre >= MOD:
                    pre -= MOD
            suma = (suma + pre * INV[c]) % MOD
        ic = INV[c]
        for s in range(n - c, -1, -1):
            if dp[s]:
                dp[s + c] = (dp[s + c] + dp[s] * ic) % MOD
    res.append(str(proba * suma % MOD))
print("\n".join(res))

