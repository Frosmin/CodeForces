def resolucion(lista):
    if len(lista) == 1:
            return "YES"
    patron = [1,0,1]
    for i in range(len(lista)-2):
        
        
        if (lista[i] == patron[0] and 
            lista[i+1] == patron[1] and 
            lista[i+2] == patron[2]):
            return "NO"
    return "YES"






n = int(input())  
 
for i in range(n):
    r = int(input())
    lista = list(map(int, input().split()))
    print(resolucion(lista))
    
