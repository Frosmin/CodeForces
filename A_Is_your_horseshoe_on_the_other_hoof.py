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





lista = list(map(int,input().split()[:4]))

dicc = {}

for numero in lista:  
    if numero in dicc:
        dicc[numero] += 1
    else:
        dicc[numero] = 1

        
tam = len(dicc)        
if tam == 4 :
    print(0)
else:
    print(4-tam)
