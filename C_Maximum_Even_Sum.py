def divi(b):
    lst =[]
    for i in range(1,b+1):
        if b % i ==0:
            lst.append(i)    
    return lst


n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    divisores = divi(b)
    res = 0
    for k in divisores:
        suma = (a*k) + (b//k)
        if suma > res and suma % 2 == 0:
            res = suma
    print(-1 if res== 0 else res)
    
