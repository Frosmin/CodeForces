def paridad(num):
    return num % 2 == 0  #true si es par

def paridad_lista(lista):
    par = 0
    impar = 0
    for n in lista:
        if paridad(n):
            par += 1
        else:
            impar += 1
    return par > impar # true si hay mas pares que impares


n = int(input())
lista = list(map(int, input().split()))
if paridad_lista(lista) == True: #mas pares
    for i in range(n):
        if paridad(lista[i]) == False:
            print(i+1)
else:
    # mas impares
    for i in range(n):
        if paridad(lista[i]) == True:
            print(i+1)