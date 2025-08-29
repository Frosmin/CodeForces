n  = int(input())
fila = list(map(int,input().split()[:n]))
maximo = max(fila)
minimo = min(fila)


pos_maximo = fila.index(maximo)  # Primera aparición del máximo
pos_minimo = len(fila) - 1 - fila[::-1].index(minimo)


res = 0
res = pos_maximo+(n-pos_minimo-1)

if pos_maximo > pos_minimo:
    res-=1

print(res)