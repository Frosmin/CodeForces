import copy

cuadrado = [[' ','2','3'], #  0
            ['4','1','5'], #  1       -1     
            ['7','8','6']] #  2    -1 0 +1
#             0   1   2               +1 
nivel = 4
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
        

def posibles_movimientos(cuadrado):
    resultado = copy.deepcopy(cuadrado)
    x , y = buscar_vacio(cuadrado)
    n = cantidad_movimientos_posibles(cuadrado)
    if cuadrado[x][y-1] != None:
            intercambiar_lugar(resultado, x, y, x, y-1)
            imprimir_cuadrado(resultado)
            resultado = copy.deepcopy(cuadrado)
            print('----------------------------------------------------------')
    if cuadrado[x][y+1] != None:
            intercambiar_lugar(resultado, x, y, x, y+1)
            imprimir_cuadrado(resultado)
            resultado = copy.deepcopy(cuadrado)
            print('----------------------------------------------------------')
    if cuadrado[x-1][y] != None:
            intercambiar_lugar(resultado, x, y, x-1, y)
            imprimir_cuadrado(resultado)
            resultado = copy.deepcopy(cuadrado)
            print('----------------------------------------------------------')
    if cuadrado[x+1][y] != None:
            intercambiar_lugar(resultado, x, y, x+1, y)
            imprimir_cuadrado(resultado)
            resultado = copy.deepcopy(cuadrado)
            print('----------------------------------------------------------')
            
        
    
    
    

print(buscar_vacio(cuadrado))
print(cantidad_movimientos_posibles(cuadrado))
posibles_movimientos(cuadrado)