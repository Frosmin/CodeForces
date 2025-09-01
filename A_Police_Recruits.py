n = int(input())
crimenes = list(map(int,input().split()[:n]))
crimenasos = 0
polis = 0

for item in crimenes:
    if item > 0:
        polis += item
    else:
        if polis != 0:
            polis -= 1
        else:
            crimenasos +=1
print(crimenasos)