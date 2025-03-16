


# keyboard = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


# def saltos(keyboard, ini, fin):
#     valor_inicio = 0 
#     valor_final =  0
#     for i in range(26):
#         if ini == keyboard[i]:
#             valor_inicio = i
#     for j in range(26):
#         if fin == keyboard[j]:
#             valor_final = j
#     return abs( valor_final - valor_inicio )


# lista = list(map(str, input()))
# res = 0
# for i in range (len(lista)):
#     if i == 25:
#         break
#     res += saltos(keyboard, lista[i], lista[i+1])
# print(res)

# print(saltos(keyboard, 'M', 'G'))



# Leer la permutación del teclado
keyboard = input().strip()

def posicion_en_teclado(keyboard, letra):
    for i in range(len(keyboard)):
        if keyboard[i] == letra:
            return i
    return -1 

res = 0
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(alfabeto) - 1): 
    letra_actual = alfabeto[i]
    letra_siguiente = alfabeto[i + 1]
    
    pos_actual = posicion_en_teclado(keyboard, letra_actual)
    pos_siguiente = posicion_en_teclado(keyboard, letra_siguiente)
    
    res += abs(pos_siguiente - pos_actual)

print(res)