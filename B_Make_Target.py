

def llenar(desde, hasta, valor, matriz):
    n = len(matriz)
    hasta = min(hasta, n)
    for fila in range(desde, hasta):
        for col in range(desde, hasta):
            matriz[fila][col] = valor 
    return matriz

def imprimir(matriz):
    for fila in matriz:
        print(''.join(str(elem) for elem in fila))
        
j = lambda n,i : n + 1 - i
n = int(input())
matriz = [['#' for i in range(n)] for j in range(n)]
if n == 1:
    print('#')
    exit()
for i in range(n):
    if i % 2 == 0:
        matriz = llenar(i-1,(j(n,i)), '.', matriz)
        
    else:
        matriz = llenar(i-1, j(n,i), '#', matriz)     
imprimir(matriz)
