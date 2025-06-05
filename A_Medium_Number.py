n = int(input())
for _ in range(n):
    lista = list(map(int, input().split()))
    lista.sort()
    print(lista[1])