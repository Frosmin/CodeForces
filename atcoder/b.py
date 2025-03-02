m1 = [['#','.','#'],['.','.','#'],['#','#','.']]

m2 = [['.','#'],['#','.']]

n=3

print(m1[1])
print(m2[0])

def es_subsecuencia(lista_pequeña, lista_grande):
    n = len(lista_pequeña)
    m = len(lista_grande)
    
    # Si la lista pequeña es más grande, no puede ser una subsecuencia
    if n > m:
        return False
        
    # Comprobamos todas las posibles posiciones iniciales
    for i in range(m - n + 1):
        if lista_grande[i:i+n] == lista_pequeña:
            return True
    return False
            

print (es_subsecuencia(m1[1], m2[0]))

# for i in range(n):
#     for j in range(n):
        
    