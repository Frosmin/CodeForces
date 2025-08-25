# Creas un diccionario vacío
mi_diccionario = {1: 2}


mi_diccionario = {}

# Añades el par clave-valor
mi_diccionario[1] = 2

print(mi_diccionario)
# Salida: {1: 2}





# Ejemplo: Un diccionario de calificaciones
calificaciones = {
    "Ana": 10,
    "Juan": 8,
    "Sofia": 10,
    "Luis": 7
}

# Comprobar si el valor 8 existe en el diccionario
if 8 in calificaciones.values():
    print("Sí, alguien obtuvo una calificación de 8.")
else:
    print("No, nadie obtuvo una calificación de 8.")

# Comprobar si el valor 5 existe
if 5 in calificaciones.values():
    print("Sí, alguien obtuvo una calificación de 5.")
else:
    print("No, nadie obtuvo una calificación de 5.")
    
    
    
    
    
#buen ejemplo pares valor 
#recorre los numero de una lista, si no existe en el dicc los pone y pone un calor, es decri que cuenta repetidos
lista = list(map(int,input().split()[:4]))

dicc = {}

for i in range(4):
    if lista[i] in dicc:
        dicc[lista[i]] +=1
    else:
        dicc[lista[i]] = 1
        
tam = len(dicc)        
if tam == 4 :
    print(0)
else:
    print(4-tam)