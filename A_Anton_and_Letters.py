
lista = input().replace(" ", "")  

dicc = {}
if lista == "{}":
    print(0)
    exit()


for i in range(len(lista)):
    if i %2 != 0:
        letra = lista[i]
        if letra in dicc:
                dicc[letra] +=1
        else:
                dicc[letra] = 1
print(len(dicc))