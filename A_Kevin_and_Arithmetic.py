


def contador_pares_impares(t):
    par = 0
    impar = 0
    for elemnto in t:
        if elemnto % 2 == 0:
            par +=1
        else:
            impar +=1
    return par, impar


def resolucion(par, impar):
    if impar == 0:
        return 1
    elif par == 0:
        return impar-1
    else:
        return impar+1
    
    


n = int(input())
for i in range(n):
    r = int(input())
    t = list(map(int ,input().split()))
    par, impar = contador_pares_impares(t)
    res = resolucion(par, impar)
    print(res)


