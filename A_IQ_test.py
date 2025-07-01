def paridad(num):
    return num % 2 == 0

def paridad_lista(lista):
    par = 0
    impar = 0
    for n in lista:
        if paridad(n):
            par += 1
        else:
            impar += 1
    return par < impar # true si hay más impares que pares


n = int(input())
lista = list(map(int, input().split()))
if paridad_lista(lista):
    for i in lista:
        if paridad(i):
            print(i)
else:
    for i in lista:
        if paridad(i) == False:
            print(i)