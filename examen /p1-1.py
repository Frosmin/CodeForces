h,e = map(int,input().split())
hoteles = list(map(int,input().split()))
elencos = list(map(int,input().split()))

e = len(elencos)
h = len(hoteles)

lista_res = []

for i in range(e):
    for j in range(h):
        if elencos[i] <= hoteles[j]:
            hoteles[j] -= elencos[i]
            lista_res.append(j+1)
            break

    else:
        lista_res.append(0)
    

    
print(*lista_res)
    
