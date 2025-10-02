lst = list(map(int,input().split()[:4]))


maximo = max(lst)
maximo_index  = lst.index(maximo)

lst.pop(maximo_index)

c = lst[0] + lst[1] - maximo
a = lst[0] - c
b = lst[1] - c

print(c,a,b)



