



for _ in range(int(input())):
    x,y = map(int,input().split())
    a,b = map(int,input().split())
    res = 0


    minimo = min(x,y)
    if (2*a) > b:
        x,y = x-minimo,y-minimo
        res+= minimo*b
        maximo= max(x,y)
        res+= maximo*a
    else:
        res += a*(x+y)


    print(res)