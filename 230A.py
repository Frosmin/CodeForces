fuerza, n = map(int, input().split())
tupla = []




def dragones(fuerza, n):    
    for i in range(n):
        df, dv = map(int, input().split())
        tupla.append((df, dv))    
    tupla.sort()
    for i in range(n):
        if fuerza > tupla[i][0]:
            fuerza += tupla[i][1]
        else:
            return False
    

if dragones(fuerza, n):
    print("YES")
else:
    print("NO")