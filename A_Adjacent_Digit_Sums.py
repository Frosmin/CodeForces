def son_nueve(numero):
    lista = list(map(int, str(numero)))
    for item in lista:
        if item != 9:
            return False
    return True

def multiplo_nueve(numero):
    if numero % 9 == 0:
        return True 
    return False

def resultado(x,y):
    if y > x + 1:
        return "NO"
    diferencia = y - x
    if (diferencia - 1) % (-9) == 0 and diferencia <= 1:
        return "YES"
    else:
        return "NO"


n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    print(resultado(x,y))
    
    
