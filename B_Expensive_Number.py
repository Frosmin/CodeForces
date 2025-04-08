# t = int(input())
# for _ in range(t):
#     n = len(str(input()))
#     if n % 2 == 0:
#         print(n//2)
#     else:
#         print(n-1) 

def eliminar_numeros(n):
    res = 0
    for i in range(len(n)):
        if n[i] != '0':
            res +=1
    return res-1

def contar_ceros_finales(s):
    cont = 0
    for char in s[::-1]:
        if char == '0':
            cont += 1
        else:
            break        
    return cont
    

t = int(input())
for _ in range(t):
    n = str(input())
    print(eliminar_numeros(n) + contar_ceros_finales(n))