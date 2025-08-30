# t  = int(input())
# for _ in range(t):
#     n,k = map(int, input().split())
#     lista = list(map(int,input().split()[:n]))
#     maximo = max(lista, key=lista.count)
#     maximo_count = lista.count(maximo)
#     target = lista.count(k)
#     print(maximo_count)
#     print(target)
#     print(maximo)
    
#     print("YES" if maximo == k or maximo_count == target else "NO")
    
    
t  = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    lista = list(map(int,input().split()[:n]))
    bb = True
    for item in lista:
        if item == k:
            print("YES")
            bb = False
            break
    if bb:
        print("NO")