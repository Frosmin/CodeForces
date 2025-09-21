requeridos, n = map(int,input().split())
lst = list(map(int,input().split()[:n]))
lst.sort()

# print(lst)
maximo = lst[-1]


for i in range(n-requeridos+1):
    if lst[i+requeridos-1]-lst[i] < maximo:
        maximo = lst[i+requeridos-1] - lst[i]
print(maximo)
