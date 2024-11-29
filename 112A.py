
# def letra_a_numero(letra):
#     return ord(letra.lower()) - ord('a') + 1


# def valor_de_lista(lista):
#     valor = 0
#     for i in range (0, len(lista)):
#         valor += letra_a_numero(lista[i])
#     return valor


# def main():
    
#     try:
       
#             lista1 = list(map(str,input().lower().strip()))
#             lista2 = list(map(str,input().lower().strip()))
            
#             if len(lista1) != len(lista2):
#                 raise ValueError("Las cadenas deben tener la misma longitud")
            
#             if valor_de_lista(lista1) == valor_de_lista(lista2):
#                  print(0)
#             elif valor_de_lista(lista1) > valor_de_lista(lista2):
#                  print(1)
#             else:
#                 print(-1)
          
#     except ValueError as e:
#         print(f"Error: {e}")
    
    
# if __name__ == "__main__":
#     main()

def letra_a_numero(letra):
    return ord(letra.lower()) - ord('a') + 1

def comparar_lexicograficamente(lista1, lista2):
    for i in range(len(lista1)):
        val1 = letra_a_numero(lista1[i])
        val2 = letra_a_numero(lista2[i])
        
        if val1 < val2:
            return -1
        elif val1 > val2:
            return 1
    return 0

def main():
    try:
        
        lista1 = list(input().lower().strip())
        lista2 = list(input().lower().strip())
        
        
        if len(lista1) != len(lista2):
            raise ValueError("Las cadenas deben tener la misma longitud")
            
        print(comparar_lexicograficamente(lista1, lista2))
          
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()