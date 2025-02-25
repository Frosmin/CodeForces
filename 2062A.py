
# def contador_unos(t):
#     cont = 0
#     for i in range(0, len(t)):
#         if t[i] == "1":
#             cont += 1
#     return cont

# def ejer(t):
#     cont = 0            
#     for j in range (0, len(t)-2):
#             if t[j] == "1" and t[j+1] == "0" and t[j+2] == "1":
#                 t[j] = "0"
#                 t[j+1] = "1"
#                 t[j+2] = "0"
#                 cont+=1
#     print(t.count("1") +cont)



# lista = []  
# n = int(input())
# for i in range(n):
#         t = list(map(str ,input()))
#         lista.append(t)
# for i in range(n):
#     ejer(lista[i])
        
        
lista = []  
n = int(input())
for i in range(n):
        t = list(map(str ,input()))
        lista.append(t)
for i in range(n):
    print(lista[i].count("1"))






