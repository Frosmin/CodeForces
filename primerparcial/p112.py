n = int(input())
lista = [[] for _ in range(n)]
mitad = n // 2

for i in range(n):
    num_palabra, palabra = input().split()
    num = int(num_palabra)
    if i < mitad:
        palabra = "-"
    lista[num].append(palabra)

lista_res = []
for num in range(n):
    for p in lista[num]:
        lista_res.append(p)

print(*lista_res)
