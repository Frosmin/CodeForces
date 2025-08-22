# n = int(input())
# amigos = list(map(int,input().split()[:n]))



# nueva_lista = []

# for i in range(n):
#     amigo = amigos[i]
#     if amigo == n:
#         amigo = 0
#     nueva_lista.append(amigos[amigo])
# print(nueva_lista)



n = int(input())
amigos = list(map(int,input().split()[:n]))

nueva_lista = [0]*4

for i in range(n):
    indice = amigos.index(amigos[i])
    print(indice)


print(nueva_lista)