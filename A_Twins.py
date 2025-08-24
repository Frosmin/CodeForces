n = int(input())
monedas = list(map(int,input().split()[:n]))


suma = sum(monedas)
necesario = suma//2
sumatoria = 0
# res = 0  
# cantidad_monedas = 0
# i = 0 
# while res <= necesario:
#     sumita = res+monedas[i]
#     if sumita <= necesario:
#         res = res+monedas[i]
#         cantidad_monedas+=1
#     i+=1
# print(res)
# print(cantidad_monedas) 


if n == 1:
    print(1)

for i in range(n):
    if sumatoria < necesario:
        sumatoria += monedas[i]
    elif sumatoria == necesario:
        sumatoria += monedas[i]
        print(i+1)
        # print(sumatoria)
        exit()
    else:
        print(i+1)
        # print(sumatoria)
        exit()