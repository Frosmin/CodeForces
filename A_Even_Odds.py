t,n = map(int,input().split())
if t % 2 ==0:
    impares = t//2
else:
    
    impares = (t//2) +1

if impares <n:
    numero_buscar = n-impares
    print(2*numero_buscar)

else:
    print(2*n-1)