lista = []
count = 0
for i in range(12):
    s = input()
    lista.append(s)
for i in range(12):
    if i+1 == len(lista[i]):
        count += 1 
print(count)