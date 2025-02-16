# palabras = input().split()
# print(palabras)


# for i in range(0, len(palabras)):
#     cont = 0
#     for j in range(0, len(palabras)-1):
#         if palabras[i] == palabras[j]:
#             cont += 1
#     print(f"{palabras[i]} --> {cont}")
#     cont = 0
# del palabras[i]
            


palabras = input().split()
palabras_procesadas = []

for palabra in palabras:
    # Solo procesa palabras que no hemos visto antes
    if palabra not in palabras_procesadas:
        palabras_procesadas.append(palabra)
        cont = palabras.count(palabra)
        print(f"{palabra} --> {cont}")