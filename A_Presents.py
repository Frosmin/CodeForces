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
posiciciones = list(map(int,input().split()[:n]))
nueva_lista= [0]*n
i = 0
while i < n:
    posicion = (posiciciones[i])-1
    nueva_lista[posicion] = i+1
    i+=1

print(" ".join(map(str,nueva_lista)))