from math import sqrt

def criba_eratostenes(n):

    es_primo = [True] * (n + 1)
    

    es_primo[0] = es_primo[1] = False
    

    for p in range(2, int(n**0.5) + 1):
        if es_primo[p]:
            for multiplo in range(p * p, n + 1, p):
                es_primo[multiplo] = False
                
    primos = set()
    for i in range(2, n + 1):
        if es_primo[i]:
            primos.add(i)
            
    return primos


n = int(input())
lst = list(map(int, input().split()[:n]))
new_list = []

primos_lista = criba_eratostenes(int(sqrt(max(lst))))

for item in lst:
    if sqrt(item).is_integer():
        if sqrt(item) in primos_lista:
            print("YES")
            continue
    print("NO")
    




