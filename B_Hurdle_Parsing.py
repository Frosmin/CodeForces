def dibujar(n):
    print('-'* n + '|', end='')
    


n = list(map(str, input()))
cont = 0
for i in range(len(n)) :
    if n[i] == '|' and  i!= 0:
        print(str(cont) + ' ', end='')
        cont = 0
        
    if n[i] == '-':
        cont += 1
    