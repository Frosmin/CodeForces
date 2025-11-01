n = int(input())
a = list(map(int, input().split()[:n]))
antes = 0
res = 0
for num in a:
    if num == 0:
        res += 1
        antes = 0
    elif num == 1:
        if antes == 1:
            res += 1
            antes = 0
        else:
            antes = 1
    elif num == 2:
        if antes == 2:
            res += 1
            antes = 0
        else:
            antes = 2
    elif num == 3:
        if antes == 1:
            antes = 2
        elif antes == 2:
            antes = 1
print(res)