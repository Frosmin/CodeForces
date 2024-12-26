n = input()
lista = list(map(str, input().strip()))

if not (len(lista) == int(n)):
    raise ValueError("Error")
r = 0
if not (len(lista) >= 1 and len(lista) <= 50):
    raise ValueError("Error")


for i in range(len(lista)):
    
    if i+1 < len(lista):
        if (lista[i] == lista[i+1]):
            r += 1
    else:
        break
        
print(lista)
print(r)