

def llenar(desde, hasta, valor, matriz):
    for fila in range(desde, hasta):
        for col in range(desde, hasta):
            matriz[fila][col] = valor 
    return matriz


def imprimir(matriz):
    for fila in matriz:
        print(fila)



j = lambda n,i : n + 1 - i


n = int(input())
matriz = [[0 for i in range(n)] for j in range(n)]
print(j(n,1))
for i in range(n-1):
    if i % 2 == 0:
        res = llenar(i+1,(j(n,i)), '*', matriz)
        imprimir(res)
    else:
        res = llenar(i+1, j(n,i), '#', matriz)
        imprimir(res)
  