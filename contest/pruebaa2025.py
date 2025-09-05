n = int(input())
for _ in range(n):
    num = int(input())
    dijitos = len(str(num))
    target = 10**dijitos
    res = abs(num-target)
    print(res)