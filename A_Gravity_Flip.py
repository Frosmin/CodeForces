# n = int(input())

# cubos = list(map(int,input().split()[:n]))

# ordenados = sorted(cubos)
# print(cubos)
# print(ordenados)
# if ordenados == cubos:
#     print(" ".join(map(str,cubos)))
# else:
#     if cubos[0] > cubos[n-1]:
#         cubos[0] ,cubos[n-1] = cubos[n-1],cubos[0]
        
        
        
n = int(input())

cubos = list(map(int,input().split()[:n]))

ordenados = sorted(cubos)
print(" ".join(map(str,ordenados)))
