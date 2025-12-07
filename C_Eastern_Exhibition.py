 
def calc(a):
    n = len(a)
    if n & 1:
        return 1
    a.sort()
    return a[n // 2] - a[n // 2 - 1] + 1
 

for _ in range(int(input())):
    n = int(input())
    a, b = [], []
    for _ in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    print(calc(a) * calc(b))
 