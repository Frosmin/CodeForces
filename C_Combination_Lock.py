import itertools

def generar_permutaciones(lista):
    permutaciones_tuplas = itertools.permutations(lista)
    permutaciones_listas = [list(perm) for perm in permutaciones_tuplas]
    permutaciones_listas.pop(0)
    return permutaciones_listas

def coincide(n, permutado, lsita):
    for i in range(n):
        if permutado[i] == lsita[i]:
            return True
    return False

def buscar_bloqueado(n, permutado , lista):
    for i in range(n):
        if coincide(n, permutado, lista):
            permutado.append(permutado.pop(0))
        else:
            return False
    return True
        


cant = int(input())
for _ in range(cant):
    n = int(input())
    lista = list(range(1,n+1)) #numeros
    permutaciones = generar_permutaciones(lista)

    for i in range(len(permutaciones)):
        if buscar_bloqueado(n, permutaciones[i], lista):
            print(' '.join(map(str, permutaciones[i])))
            break
    else:
        print(-1)

        
