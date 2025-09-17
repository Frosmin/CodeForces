t = int(input())
for _ in range(t):
    num  = list(map(int, input()))
    tam = len(num)
    res = []
    for i in range(tam):
        if num[i]!=0:
            res.append(num[i]*10**(tam-i-1))
    print(len(res))
    print(*res)

    