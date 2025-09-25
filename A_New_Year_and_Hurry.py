problems , mins = map(int, input().split())
tiempo_tiene = 240-mins
resta = 1
p = 0


while tiempo_tiene >= resta*5 and p < problems:
    tiempo_tiene -= resta*5
    p+=1
    resta+=1

print(p)
