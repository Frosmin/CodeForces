# def iguales_cantidad(dado1,dado2,dado3):
#     num_iguales = 0
#     mayores = []
#     menores = []
#     if dado1 >= dado2:
#         if dado1 >=
        


def probabilidad_ganar(dado1, dado2):
    ganar = 0
    perder = 0
    for num1 in dado1:
        for num2 in dado2:
            if num1 > num2:
                ganar +=1
            else:
                perder +=1
    if ganar + perder == 0:
        return 0
    else:
        return ganar/(ganar+perder)
    


dado1 = list(map(int,input().split()[:6])) 
dado2 = list(map(int,input().split()[:6])) 
dado3 = list(map(int,input().split()[:6])) 

probailidad = []

if dado1 == dado2 and dado2 == dado3:
    print(1)
    exit()
    
probailidad_ganar1=probabilidad_ganar(dado1,dado2) + probabilidad_ganar(dado1,dado3)
probailidad_ganar2=probabilidad_ganar(dado2,dado1) + probabilidad_ganar(dado2,dado3)
probailidad_ganar3=probabilidad_ganar(dado3,dado1) + probabilidad_ganar(dado3,dado2)
# print(probailidad_ganar1)
# print(probailidad_ganar2)
# print(probailidad_ganar3)

if probailidad_ganar3 == probailidad_ganar2 == probailidad_ganar1:
    print("No dice")
    exit()



probabilidades = [probailidad_ganar1,probailidad_ganar2,probailidad_ganar3]
mayor = 0
cant = 0
posicion = 0
for i in range(3):
    if probabilidades[i] == mayor:
        cant+=1
    
    elif probabilidades[i] > mayor:
        mayor = probabilidades[i]
        posicion = i+1


print("No dice" if cant > 1 else posicion)


# if cant > 1:
#     print("No dice")
# else:
#     print(posicion)
    
    
    
# print(posicion)    
# print(cant) 
    
    
# if probabilidad_ganar(dado1,dado2) + probabilidad_ganar(dado1,dado3) >= 1:
#     print(probabilidad_ganar(dado1,dado2) + probabilidad_ganar(dado1,dado3))
#     print(1)
#     exit()
# elif probabilidad_ganar(dado2,dado1) + probabilidad_ganar(dado2,dado3) >= 1:
#     print(probabilidad_ganar(dado2,dado1) + probabilidad_ganar(dado2,dado3) )
#     print(2)
#     exit()
# elif probabilidad_ganar(dado3,dado1) + probabilidad_ganar(dado3,dado2) >= 1:
#     print(probabilidad_ganar(dado3,dado1) + probabilidad_ganar(dado3,dado2))
#     print(3)
#     exit()


# lista = [dado1,dado2,dado3]


# maximo = 0
# cont = 0
# indice = 0
# for i in range(3):
#     suma_dado = sum(lista[i])
#     if suma_dado > maximo:
#         maximo = suma_dado
#         indice = i
#     elif suma_dado == maximo:
#         cont+=1
# print(indice+1)





# print(probabilidad_ganar(dado1, dado2))
# print(probabilidad_ganar(dado1, dado3))

# print(probabilidad_ganar(dado2, dado1))
# print(probabilidad_ganar(dado2, dado3))

# print(probabilidad_ganar(dado1, dado2))
# print(probabilidad_ganar(dado1, dado3))
