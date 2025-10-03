def es_dfs_valido(n, p):
    # p debe empezar con 1 (la raíz)
    if p[0] != 1:
        return False
    
    # Creamos un mapa de posición para cada elemento
    pos = {}
    for i in range(n):
        pos[p[i]] = i
    
    # Verificamos cada nodo
    for i in range(n):
        nodo = p[i]
        
        # Calculamos los hijos
        hijo_izq = 2 * nodo
        hijo_der = 2 * nodo + 1
        
        # Si el nodo tiene hijos
        if hijo_izq <= n:
            # Los hijos deben estar después del padre
            if pos[hijo_izq] <= i or pos[hijo_der] <= i:
                return False
            
            # Los hijos deben estar consecutivos
            pos_izq = pos[hijo_izq]
            pos_der = pos[hijo_der]
            
            if abs(pos_izq - pos_der) != 1:
                return False
            
            # El siguiente después del padre debe ser uno de los hijos
            if i + 1 < n:
                siguiente = p[i + 1]
                if siguiente != hijo_izq and siguiente != hijo_der:
                    return False
    
    return True


for _ in range(int(input())):
    n, q = map(int, input().split())
    padres = list(map(int, input().split()))
    p = list(map(int, input().split()))
    
    for _ in range(q):
        x, y = map(int, input().split())
        # Swap (convertir a índices 0-based)
        x -= 1
        y -= 1
        p[x], p[y] = p[y], p[x]
        
        # Verificar si es DFS válido
        if es_dfs_valido(n, p):
            print("YES")
        else:
            print("NO")