def funcion(cabezas, caballeros):
    oro = 0
    while cabezas and caballeros:   
        
        if cabezas[0] <= caballeros[0]:
            oro += caballeros[0]
            cabezas.pop(0)
            caballeros.pop(0)
        else:
            caballeros.pop(0)
    if cabezas:
        return "Loowater is doomed!"
    else:
        return oro










while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    cabezas = []
    caballeros = [] 
    for _ in range(n):
        cabezas.append(int(input())) 
    for _ in range(m):
        caballeros.append(int(input()))
    
    print(funcion(sorted(cabezas), sorted(caballeros)))
                
    