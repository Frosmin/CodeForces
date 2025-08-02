def full_upper(lista):
    if all(elemento.isupper() for elemento in lista):
        return True
    else:
        return False

def full_lower(lista):
    if all(elemento.islower()for elemento in lista):
        return True
    else:
        return False




def caps(lista):
    if len(lista) == 1 :
        if lista[0].isupper():
            lista[0] = lista[0].lower()
        else:
            lista[0] = lista[0].upper()
    elif full_upper(lista):
        for i in range(len(lista)):
            lista[i] = lista[i].lower()
    elif full_lower(lista):
        pass
    elif lista[0].isupper():
        pass
    elif full_upper(lista[1:]):
        lista[0] = lista[0].upper()
        for i in range(len(lista)-1):
            lista[i+1]=lista[i+1].lower()
    elif lista[0].islower():
        pass



palabra = list(map(str, input()))
caps(palabra)
print("".join(palabra))
