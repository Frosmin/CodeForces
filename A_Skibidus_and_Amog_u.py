n = int(input())
for _ in range(n):
    lista = list(map(str, input()))
    lista = lista[:-2]
    lista.append('i')
    print(''.join(lista))