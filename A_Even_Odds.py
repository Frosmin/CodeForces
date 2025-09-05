t,n = map(int,input().split())
impares = (t//2) +1

if impares <n:
    numero_buscar = t- impares
    pares = list(range(2, 2*numero_buscar + 1, 2))
    print(pares[numero_buscar-1])
else:
    
    impares = list(range(1, 2*n, 2))
    print(impares[n-1])