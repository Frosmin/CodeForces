t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int,input()[:n]))
    ceros = lst.count(0)
    res = 0
    for i in range(ceros):
        if lst[i] == 1 :
            res+=1
    print(res)

            