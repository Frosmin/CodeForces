def posiciones(n, k, list):
    cont = 0
    inicio = 0
    fin = 0
    anterior = 0
    for i in range(n):
        if cont == k:
            fin = i-1
            break
        if list[i] == 1 and i == n-1:
            cont += 1
            fin = i
            break
            
        if cont == k-2 and list[i] == 1 and list[i+1] == 0:
            anterior = i   
        if list[i] == 0 and list[i+1] == 1:
            inicio = i+1
        if list[i] == 1 and  list[i+1] == 0:
            cont += 1
    return inicio, fin, anterior
n, k = map (int,input().split())
list = list(map(int, input()))
ini, fin, anter = posiciones(n, k, list)
segmento = list[ini:fin+1]
nueva_lista = list[:ini] + list[fin+1:]
resultado = nueva_lista[:anter+1] + segmento + nueva_lista[anter+1:]

print(''.join(map(str, resultado)))
