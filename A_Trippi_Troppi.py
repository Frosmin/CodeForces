n = int(input())

for _ in range(n):
    lista = list(map(str, input().split()))
    for i in range(3):
        print(lista[i][0], end="")
    print()