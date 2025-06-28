# def suma(lista, T):
#     mejor_suma = 0
#     suma_actual = 0
#     for i in range(N):
#         suma_actual = lista[i]
#         for j in range(N-1):
#                 suma_actual += lista[j+1]
#                 if mejor_suma < suma_actual <= T:
#                     mejor_suma = suma_actual
#                 if suma_actual == T:
#                     return T
#                 if suma_actual < T :
#                     continue
#                 if suma_actual > T:
#                     suma_actual = lista[i]
#     return mejor_suma

        
            

# N,T = map(int, input().split())
# lista = list(map(int, input().split()))
# lista.sort(reverse=True)
# print(suma(lista, T))

def aux(arr):
    sumas = [0]
    for x in arr:
        sumas.extend([s + x for s in sumas])
    return sumas


def busqueda_binaria_le(arr, target):
    low, high = 0, len(arr) - 1
    mejor_candidato = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            mejor_candidato = arr[mid]
            low = mid + 1
        else:
            high = mid - 1
    return mejor_candidato

def suma(lista, T):
    mitad = N // 2
    primera_mitad = lista[:mitad]
    segunda_mitad = lista[mitad:]

    sumas1 = aux(primera_mitad)
    sumas2 = aux(segunda_mitad)

    
    sumas2.sort()

    mejor_suma_total = 0
    for s1 in sumas1:
        if s1 <= T:

            restante = T - s1
            
            s2 = busqueda_binaria_le(sumas2, restante)
            
            if s2 != -1:
                mejor_suma_total = max(mejor_suma_total, s1 + s2)
            else:
                mejor_suma_total = max(mejor_suma_total, s1)
    
    return mejor_suma_total

N,T = map(int, input().split())
lista = list(map(int, input().split()))
lista.sort(reverse=True)
print(suma(lista, T))