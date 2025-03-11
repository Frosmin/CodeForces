
def buscar(list,n):
    res= 0
    for i in range(n-2):
        if list[i] == '#' and list[i+1] == '.' and list[i+2] == '#':
            res += 1
    return res



n = int(input())
list = list(map(str, input()))

print(buscar(list,n))
