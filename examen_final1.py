import sys

datos = sys.stdin.read().split()
    


iterador = iter(datos)
    
try:
    while True:

        n = int(next(iterador))
        palabra1 = next(iterador)
        palabra2 = next(iterador)
     
        if palabra1 == palabra2:
            print(0)
            continue
            

            
        nueva_palabra = palabra1 + palabra1[:-1]
        index = nueva_palabra.rfind(palabra2)
            
        if index != -1:
                print(n - index)
        else:
                print(-1)
                
except StopIteration:
    pass






