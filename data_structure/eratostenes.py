from math import sqrt

def criba_eratostenes(n):
    # Creamos una lista de valores True (todos son candidatos a primos)
    primos = [True] * (n+1)
    primos[0] = primos[1] = False  # 0 y 1 no son primos

    # Solo necesito revisar hasta la raíz cuadrada de n
    p = 2
    while p * p <= n:
        if primos[p]:  # si p sigue marcado como primo
            # marcar como no primos los múltiplos de p
            for i in range(p*p, n+1, p):
                primos[i] = False
        p += 1

    # Retornar todos los índices que quedaron en True
    return [i for i, es_primo in enumerate(primos) if es_primo]




n=100
p=3
for i in range(p*p, n+1, p):
    print(i)