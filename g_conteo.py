n,k = map(int, input().split())
lista = list(map(int, input().split()))
res = 0
total = sum(lista)
for i in range(n):
    eliminar = total - lista[i]
    if eliminar % k == 0:
        res += 1
print(res)
