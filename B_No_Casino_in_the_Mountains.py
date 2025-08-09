total = int(input())
for _ in range(total):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    res = 0
    subidos = 0
    i = 0
    while i < n:
        if a[i] == 0:
            subidos += 1
            if subidos == k:
                res += 1
                subidos = 0
                i += 1
        else:
            subidos = 0
        i += 1
    print(res)