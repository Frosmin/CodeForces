for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()[:n]))
    res =0
    maximo = 0
    for item in lst:
        if item == 1:
            maximo = max(res,maximo)
            res = 0
        else:
            res+=1
    maximo = max(res,maximo)



    print(maximo)