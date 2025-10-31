costos = list(map(int,input().split()))
pasos = list(map(int,input()))
res = 0
for item in pasos:
    res+= costos[item-1]

print(res)