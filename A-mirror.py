def noventa(lista,n):
    nueva_lista = []
    for i in range(n):
        x=lista[i][n-1]  
        nueva_lista.append(x)
    return nueva_lista


def dos_cetenta(lista, n):
    nueva_lista = []
    for i in range(n-1,-1,-1):
        x=lista[i][0]  
        nueva_lista.append(x)
    return nueva_lista


    


isz, der = [],[]
n  = int(input())
for _ in range(n):
    a, b = list(map(str, input().split()))
    isz.append(list(a))
    der.append(list(b))

inicial = isz[0]



if inicial == der[0]:
    print("preserved")
elif inicial == noventa(der,n):
    print(90)
elif inicial == der[n-1]:
    print("reflected")
elif inicial == dos_cetenta(der,n):
    print(270)
# elif inicial == 
#     print("reflected")

