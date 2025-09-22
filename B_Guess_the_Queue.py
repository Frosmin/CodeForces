# from collections import deque


# def sale(x,y):
#     if x =="B":
#         lst.pop()
#     else:
#         lst.popleft()


# def entra(x,y):
#     if x =="B":
#         lst.append(y)
#     else:
#         lst.appendleft(y)





# y = int(input())
# for kk in range(y):
#     n = int(input())
#     lst = deque()
#     print(f"Case {kk+1}:")
#     for _ in range(n):
#         cadena = input().split()
#         entrada = cadena[0]
#         x = cadena[1]
#         if len(cadena)> 2:
#             y = int(cadena[2])-1
#         else:
#             y = 0
        
    

#         if entrada == "1":
#             entra(x,y)
#         elif entrada == "2":
#             sale(x,y)
#         else:
#             print(lst[y])



    
    
    
# from collections import deque


# def sale(x):
#     if x == "B":
#         lst.pop()
#     else:
#         lst.popleft()

# def entra(x, y):
#     if x == "B":
#         lst.append(y)
#     else:
#         lst.appendleft(y)


# t = int(input())
# for kk in range(1, t + 1):
#     n = int(input())
#     lst = deque()
#     print(f"Case {kk}:")
#     for _ in range(n):
#         cadena = input().split()
#         operacion = cadena[0]
        
#         if operacion == "1":

#             x = cadena[1]
#             y_id = int(cadena[2])
#             entra(x, y_id)

#         elif operacion == "2":
#             x = cadena[1]
#             sale(x)

#         elif operacion == "3":
#             x = cadena[1]
#             valor = int(cadena[2])
            
#             if x == 'D':
#                 print(lst[valor - 1])
#             elif x == 'P':
#                 posicion = lst.index(valor) + 1
#                 print(posicion)
import sys


datos = sys.stdin.read().splitlines()
t = int(datos[0])
index = 1
for case_num in range(1, t+1):
    n = int(datos[index]); index += 1
    operations = []
    for i in range(n):
        partes = datos[index].split()
        index += 1
        operations.append(partes)
    
    tam = 2 * n + 10
    arr = [0] * tam
    front = n
    back = n - 1
    mapa = {}
    respuestas = []
    
    for op in operations:
        if op[0] == '1':
            x = op[1]
            y = int(op[2])
            if x == 'B':
                back += 1
                arr[back] = y
                mapa[y] = back
            else: # 'F'
                front -= 1
                arr[front] = y
                mapa[y] = front
        elif op[0] == '2':
            x = op[1]
            if x == 'B':
                back -= 1
            else: 
                front += 1
        else:
            x = op[1]
            y = int(op[2])
            if x == 'D':
                poss = front + y - 1
                respuestas.append(str(arr[poss]))
            else:
                id = mapa[y]
                position = id - front + 1
                respuestas.append(str(position))
                
    print(f"Case {case_num}:")
    for ans in respuestas:
        print(ans)