n = int(input())
monedas = list(map(int,input().split()[:n]))
monedas= sorted(monedas,reverse=True)



suma = sum(monedas)

necesario = suma/2
sumatoria = 0

if n == 1:
    print(1)
    exit()
i = 0
while sumatoria <= necesario:
    sumatoria+=monedas[i]
    i+=1

print(i)