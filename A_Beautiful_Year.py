def repetidos(lista):
    for item in lista:
        if lista.count(item) > 1:
            return False
    return True 

def lista_a_numero(lista_enteros):
    return int(''.join(map(str, lista_enteros)))
def numero_a_lista(numero):
    return list(map(int, str(numero)))

def busacar_numero(numeroLista):
    
    numero = lista_a_numero(numeroLista)
    numero += 1
    lista = numero_a_lista(numero)
    
    while repetidos(lista) == False:
        numero = lista_a_numero(lista)
        numero += 1
        lista = numero_a_lista(numero)
    print(numero)

lista = list(map(int, input()))
busacar_numero(lista)