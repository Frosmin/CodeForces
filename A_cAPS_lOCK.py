def caps(lista):
    lista[0] = lista[0].upper()
    for i in range(len(lista)-1):
        lista[i+1]=lista[i+1].lower()


palabra = list(map(str, input()))
caps(palabra)
print("".join(palabra))
