






def respuesta():
    n = int(input())
    permutacion = list(map(int, input().split()[:n]))

    intercambios = 0
    tamano_bloque = 2
    while tamano_bloque <= n:
        for i in range(0, n, tamano_bloque):
            mitad_tamano = tamano_bloque // 2
            inicio_izquierda = i
            inicio_derecha = i + mitad_tamano


            valor_izquierda = permutacion[inicio_izquierda]
            valor_derecha = permutacion[inicio_derecha]

 
            if abs(valor_izquierda - valor_derecha) != mitad_tamano:
                print(-1)
                return


            if valor_izquierda > valor_derecha:
                intercambios += 1

                for j in range(mitad_tamano):
                    permutacion[inicio_izquierda + j], permutacion[inicio_derecha + j] = \
                        permutacion[inicio_derecha + j], permutacion[inicio_izquierda + j]
        

        tamano_bloque *= 2

    print(intercambios)




for _ in range(int(input())):
    respuesta()


# import math

# def pares(lst, resultado):
#     for i in range(0,n-1,2):
#         if abs(lst[i] - lst[i+1]) == 1:
#             if lst[i] > lst[i+1]:
#                 resultado+=1
#         else:
#             print(-1)
#             return



# def swap(lst, resultado): 
 
#         if len(lst)== 2:
#             return

#         mitad = len(lst)//2
#         res1 = 0
#         res2= 0
#         primera_mitad = lst[:mitad]
#         segunda_mitad = lst[mitad:]



#         for i in range(mitad):
#             if primera_mitad[i] > mitad:
#                 res1+=1
#             else:
#                 res2 +=1

#         if max(res1,res2) == mitad:

#             if res1 == mitad:
#                 resultado+=1

#             swap(primera_mitad,resultado)
#             swap(segunda_mitad,resultado)
        



            
            

#             # mitad1= list(range(1,mitad+1))
#             # mitad2 = list(range(mitad+1,n+1))
#             # for i in range(n-1):
#             #     if lst[i] > lst[i+1]:
#             #         ressultado+=1




            


#         else:
#             print(-1)
#             return




# for _ in range(int(input())):
#     n = int(input())
#     lst_total = list(map(int,input().split()[:n]))
#     lst = lst_total.copy()
#     resultado = 0
#     tam = math.log2(n)
#     swap(lst,resultado)
#     pares(lst_total,resultado)
#     print(resultado)



