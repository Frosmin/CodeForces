import copy

# cuadrado = [[' ','2','3'], #  0
#             ['4','1','5'], #  1       -1     
#             ['7','8','6']] #  2    -1 0 +1
# #             0   1   2               +1 
# nivel = 4
cuadrado = [['1','2',' '], 
            ['3','4','5'],
            ['6','7','8']]
meta = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', ' ']]
def buscar_vacio(cuadrado):
    for i in range(3):
        for j in range(3):
            if cuadrado[i][j] == ' ':
                return i, j
            
def cantidad_movimientos_posibles(cuadrado):
    x , y = buscar_vacio(cuadrado)
    if x == 0 or x == 2:
        if y == 0 or y == 2:
            return 2
        else:
            return 3
    else:
        if y == 1:
            return 4
        else:   
            return 3

def imprimir_cuadrado(cuadrado):
    for i in range(3):
        print(cuadrado[i])
        
def intercambiar_lugar(cuadrado, x, y, x1, y1):
    cuadrado[x][y], cuadrado[x1][y1] = cuadrado[x1][y1], cuadrado[x][y]
    return cuadrado

def es_meta(meta, lista_resultados):
    for i in range(len(lista_resultados)):
        if lista_resultados[i] == meta:
            return True
    return False
        

# def posibles_movimientos(cuadrado, meta):
#     lista_resultados = []   
#     resultado = copy.deepcopy(cuadrado)
#     x, y = buscar_vacio(cuadrado)
#     n = cantidad_movimientos_posibles(cuadrado)
    
#     # while es_meta(meta, lista_resultados) == False:
#     # Movimiento a la izquierda
#     if y > 0:  # Verifica que no estemos en el borde izquierdo
#             intercambiar_lugar(resultado, x, y, x, y-1)
#             imprimir_cuadrado(resultado)
#             resultado = copy.deepcopy(cuadrado)
#             lista_resultados.append(resultado)
#             print('----------------------------------------------------------')
        
#     # Movimiento a la derecha
#     if y < 2:  # Verifica que no estemos en el borde derecho
#             intercambiar_lugar(resultado, x, y, x, y+1)
#             imprimir_cuadrado(resultado)
#             resultado = copy.deepcopy(cuadrado)
#             lista_resultados.append(resultado)
#             print('----------------------------------------------------------')
        
#         # Movimiento hacia arriba
#     if x > 0:  # Verifica que no estemos en el borde superior
#             intercambiar_lugar(resultado, x, y, x-1, y)
#             imprimir_cuadrado(resultado)
#             resultado = copy.deepcopy(cuadrado)
#             lista_resultados.append(resultado)
#             print('----------------------------------------------------------')
        
#         # Movimiento hacia abajo
#     if x < 2:  # Verifica que no estemos en el borde inferior
#             intercambiar_lugar(resultado, x, y, x+1, y)
#             imprimir_cuadrado(resultado)
#             resultado = copy.deepcopy(cuadrado)
#             lista_resultados.append(resultado)
#             print('----------------------------------------------------------')
#     return lista_resultados




def posibles_movimientos(cuadrado):
    lista_resultados = []   
    x, y = buscar_vacio(cuadrado)
    
    # Movimiento a la izquierda
    if y > 0:  
        resultado = copy.deepcopy(cuadrado)
        intercambiar_lugar(resultado, x, y, x, y-1)
        lista_resultados.append(resultado)
        
    # Movimiento a la derecha
    if y < 2:  
        resultado = copy.deepcopy(cuadrado)
        intercambiar_lugar(resultado, x, y, x, y+1)
        lista_resultados.append(resultado)
        
    # Movimiento hacia arriba
    if x > 0:  
        resultado = copy.deepcopy(cuadrado)
        intercambiar_lugar(resultado, x, y, x-1, y)
        lista_resultados.append(resultado)
        
    # Movimiento hacia abajo
    if x < 2:  
        resultado = copy.deepcopy(cuadrado)
        intercambiar_lugar(resultado, x, y, x+1, y)
        lista_resultados.append(resultado)
        
    return lista_resultados
        

def recusivo(lista_resultados, meta):
    if es_meta(meta, lista_resultados) == False:
        results = posibles_movimientos(cuadrado)
        recusivo(results, meta)
    else:
        print('Se encontró la meta')
    

print(buscar_vacio(cuadrado))
print(cantidad_movimientos_posibles(cuadrado))
recusivo(posibles_movimientos(cuadrado), meta)


# import copy
# from collections import deque

# cuadrado = [['1','2',' '], 
#             ['3','4','5'],
#             ['6','7','8']]

# meta = [['1', '2', '3'], 
#         ['4', '5', '6'], 
#         ['7', '8', ' ']]

# def buscar_vacio(cuadrado):
#     for i in range(3):
#         for j in range(3):
#             if cuadrado[i][j] == ' ':
#                 return i, j
            
# def imprimir_cuadrado(cuadrado):
#     for i in range(3):
#         print(cuadrado[i])
        
# def intercambiar_lugar(cuadrado, x, y, x1, y1):
#     cuadrado[x][y], cuadrado[x1][y1] = cuadrado[x1][y1], cuadrado[x][y]
#     return cuadrado

# def posibles_movimientos(cuadrado):
#     lista_resultados = []   
#     x, y = buscar_vacio(cuadrado)
    
#     # Define los posibles movimientos: arriba, abajo, izquierda, derecha
#     movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
#     for dx, dy in movimientos:
#         nx, ny = x + dx, y + dy
#         # Verificar que el nuevo movimiento está dentro del tablero
#         if 0 <= nx < 3 and 0 <= ny < 3:
#             resultado = copy.deepcopy(cuadrado)
#             intercambiar_lugar(resultado, x, y, nx, ny)
#             lista_resultados.append(resultado)
            
#     return lista_resultados

# def convertir_a_tupla(cuadrado):
#     """Convierte el cuadrado en una tupla inmutable para poder usarlo como clave en un conjunto"""
#     return tuple(tuple(fila) for fila in cuadrado)

# def busqueda_en_anchura(cuadrado_inicial, meta):
#     # Cola para BFS
#     cola = deque([(cuadrado_inicial, [])])  # (estado, camino)
#     # Conjunto para estados visitados
#     visitados = {convertir_a_tupla(cuadrado_inicial)}
    
#     pasos = 0
#     max_pasos = 5000000000000000000 # Límite para evitar bucles muy largos
    
#     while cola and pasos < max_pasos:
#         pasos += 1
#         estado_actual, camino = cola.popleft()
        
#         # Verificar si es la meta
#         if estado_actual == meta:
#             print(f"¡Se encontró la meta en {len(camino)} movimientos!")
#             print("Camino recorrido:")
#             for i, estado in enumerate(camino + [estado_actual]):
#                 print(f"Paso {i}:")
#                 imprimir_cuadrado(estado)
#                 print("----------------")
#             return True
        
#         # Generar nuevos estados
#         nuevos_estados = posibles_movimientos(estado_actual)
        
#         for nuevo_estado in nuevos_estados:
#             estado_tupla = convertir_a_tupla(nuevo_estado)
#             if estado_tupla not in visitados:
#                 visitados.add(estado_tupla)
#                 nuevo_camino = camino + [estado_actual]
#                 cola.append((nuevo_estado, nuevo_camino))
    
#     if pasos >= max_pasos:
#         print("Se alcanzó el límite de pasos sin encontrar solución")
#     else:
#         print("No se encontró solución")
#     return False

# # Ejecutar la búsqueda
# print("Estado inicial:")
# imprimir_cuadrado(cuadrado)
# print("\nEstado meta:")
# imprimir_cuadrado(meta)
# print("\nIniciando búsqueda...")
# busqueda_en_anchura(cuadrado, meta)