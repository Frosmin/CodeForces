uno = 0
dos = 0
tres = 0
cuatro = 0
list = list(map(int, input().split()))
for item in list:
    if item == 1:
        uno += 1
    elif item == 2:
        dos += 1
    elif item == 3:
        tres += 1
    else:
        cuatro += 1
res = 0

res = uno//2 + dos//2 + tres//2 + cuatro//2
print(res)