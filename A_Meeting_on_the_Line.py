for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    maximo,minimo =0,float('inf')
    for x,y in zip(a,b):
        maximo = max(maximo,x+y)
        minimo = min(minimo,x-y)
 
    print((maximo+minimo)/2)